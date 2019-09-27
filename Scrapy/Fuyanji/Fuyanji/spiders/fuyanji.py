# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
from Fuyanji.items import FuyanjiItem


class FuyanjiSpider(scrapy.Spider):
    name = 'fuyanji'
    allowed_domains = ['www.shuyaya.cc']
    start_urls = ['https://www.shuyaya.cc/read/4531/']

    # 抓取目录页的标题链接
    def parse(self, response):
        links = response.xpath("/html/body/div[5]/div[3]/ul/li/a/@href").extract()
        for link in links:
            yield scrapy.Request(url=parse.urljoin(response.url, link), callback=self.parse_page)

    # 抓取文章页面的标题和内容，并对文章的内容进行整理。
    def parse_page(self, response):
        item = FuyanjiItem()
        texts = response.xpath("//*[@id=\"content\"]/text()").extract()
        text_contents = ""
        for text in texts:
            text = text.replace("\xa0" * 8, "")
            text_contents += text + "\n"
        item['text'] = text_contents
        item['title'] = response.css(".read_body h1::text").extract_first()
        yield item
