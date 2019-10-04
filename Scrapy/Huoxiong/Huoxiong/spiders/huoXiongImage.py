# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy import FormRequest
import json
from Huoxiong.items import HuoxiongItem


class HuoxiongimageSpider(scrapy.Spider):
    name = 'huoXiongImage'  # 这个name必不可少。
    allowed_domains = ['cgartt.com']
    start_urls = ['http://cgartt.com/']
    base_url_1 = "http://cgartt.com/api/api.php?d=index&c=Index&action=getWorkList"
    base_url_2 = "http://cgartt.com/index_writing_detail.php?work=0&id="
    base_url_3 = "http://cgartt.com/api/api.php?d=find&c=FindInfo&action=getWorkDetial"

    # 爬取前10页。
    def start_requests(self):
        for page in range(1, 11):
            data = {'order': 2}
            data['page'] = page
            # 提交表单，为了得到最新上传一栏的1到10页的json。
            yield Request(url=self.base_url_1, method='POST', body=json.dumps(data), callback=self.parse)

    # 分析提交表单后得到的数据。
    def parse(self, response):
        text = response.text
        text = text[18:]
        text = json.loads(text)
        for list in text['list']:
            id = list['id']
            url = self.base_url_2 + id
            yield Request(url=url, callback=self.parse_page, meta={'id': id}) # 这个meta里面不总是item的。

    def parse_page(self, response):
        id = response.meta['id']  # 这个不能写成response['id']
        data = {'id': id}
        # 不知怎么的，用FormRequest能得到需要的数据，而Request不能，所以一个不能用时，考虑用另一个。
        yield FormRequest(url=self.base_url_3, formdata=data, method='POST', callback=self.parse_detail)

    # 在图片页面获取图片的链接用于下载。另外也获取图片的id，标题和作者。
    def parse_detail(self, response):
        text = response.text
        text = text[8:]
        text = json.loads(text)
        images = text['worksInfo'][0]
        for image in images['imageUrl']:
            item = HuoxiongItem()
            item['img'] = image['imageUrl']
            item['title'] = images['title']
            item['Name'] = images['username']
            item['id'] = images['id']
            yield item
