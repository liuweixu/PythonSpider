# -*- coding: utf-8 -*-
import scrapy
from Bing.items import BingItem


class BingImagesSpider(scrapy.Spider):
    name = 'bing_images'
    allowed_domains = ['bing.plmeizi.com']
    start_urls = ['http://bing.plmeizi.com/']

    def parse(self, response):
        base_url = "http://bing.plmeizi.com/?page="
        for page in range(1, 129):
            url = base_url + str(page)
            yield scrapy.Request(url, callback=self.parse)
        # 这个有必要进行循环，因为在pipeline.py 中scrapy.Request()里面的url是需要url的，而不是一个列表的。
        for image in response.css(".clearfix .item"):
            item = BingItem()
            item['url'] = image.css("div img::attr(src)").extract_first()
            item['title'] = image.css("p::text").extract_first()
            yield item
