# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
from Jipin.items import JipinItem


class JipinjiadingSpider(scrapy.Spider):
    name = 'jipinjiading'
    allowed_domains = ['www.biqukan.com']
    start_urls = ['http://www.biqukan.com/3_3053/']

    # 抓取目录页的标题的链接
    def parse(self, response):
        links = response.css(".listmain dl dd a::attr(href)").extract()
        for link in links:
            yield scrapy.Request(url=parse.urljoin(response.url, link), callback=self.parse_page)

    # 抓取文章页面的标题和内容。
    def parse_page(self, response):
        item = JipinItem()
        item['title'] = response.css(".content h1::text").extract_first()
        texts = response.xpath("//*[@id=\"content\"]/text()").extract()
        item['text'] = "".join(texts).replace("\xa0" * 8, "")
        yield item
