# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlencode
import json
from Banciyuan.items import BanciyuanItem


class BanciyuanSpider(scrapy.Spider):
    name = 'banciyuan'
    allowed_domains = ['bcy.net/illust']
    start_urls = ['https://bcy.net/illust/toppost100/']

    def start_requests(self):
        data = {'ttype': 'illust', 'sub_type': 'week', 'date': '20190928'}
        base_url = 'https://bcy.net/apiv3/rank/list/itemInfo?'
        for page in range(1, self.settings.get('MAX_NUM') + 1):
            data['p'] = page
            url = base_url + urlencode(data)
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        result = json.loads(response.text)
        for image in result.get('data').get('top_list_item_info'):
            item = BanciyuanItem()
            item['id'] = image.get('item_detail').get('item_id')
            item['cover'] = image.get('item_detail').get('cover')
            # print(item['cover'])
            image['name'] = image.get('item_detail').get("uname")
            yield item
