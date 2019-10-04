# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from BilibiliPhotos.items import BilibiliphotosItem
from urllib.parse import urlencode
import json


class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['h.bilibili.com']
    start_urls = ['https://h.bilibili.com/eden/draw_area#/all/hot/']
    base_url = "https://api.vc.bilibili.com/link_draw/v2/Doc/list?category=all&type=hot&"

    # 先爬取前200张最热的图片。必须用start_requests(self)。
    def start_requests(self):
        param = {
            'page_size': 20,
        }
        for page_num in range(10):
            param['page_num'] = page_num
            url = self.base_url + urlencode(param)
            yield Request(url, callback=self.parse)
    # 解析
    def parse(self, response):
        result = json.loads(response.text)
        for it in result.get('data').get('items'):
            for image in it.get('item').get('pictures'):
                item = BilibiliphotosItem()
                item['img'] = image['img_src']
                item['title'] = it['item']['title']
                yield item
