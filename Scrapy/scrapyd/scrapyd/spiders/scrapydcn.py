# -*- coding: utf-8 -*-
import scrapy
from scrapyd.items import ScrapydItem
from urllib import parse


class ScrapydcnSpider(scrapy.Spider):
    name = 'scrapydcn'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/']

    def parse(self, response):
        page_links = response.xpath('//*[@id="main"]/ol/li/a/@href').extract()
        # print("fsd")
        for page_link in page_links:
            # print(page_link)
            yield scrapy.Request(url=page_link, callback=self.parse)
        item = ScrapydItem()
        item['Title'] = response.xpath("//*[@id=\"logo\"]/text()").extract_first()
        links = response.xpath("//*[@id=\"main\"]/div/span[2]/a/@href").extract()
        for link in links:
            yield     scrapy.Request(url=parse.urljoin(response.url, link), meta={"meta_1": item}, \
                   callback=self.parse_page)

    def parse_page(self, response):
        item = response.meta['meta_1']
        # 抓取文章页面的文字内容
        item['text'] = self.get_text(response)
        # 抓取文章的标签
        item['tag'] = self.get_tag(response)
        # 抓取文章的标题
        item['title'] = self.get_title(response)
        # 抓取文章的图片
        item['image'] = self.get_image(response)
        yield item

    def get_text(self, response):
        text_content = ""
        text_list = response.xpath('//*[@id="main"]/article/div/p[1]').extract()
        for text in text_list:
            text_content += text.replace("<p>", "").replace("</p>", "").replace("<br>", "\n")
        return text_content

    def get_tag(self, response):
        return response.xpath('//*[@id="main"]/article/p/a/text()').extract()

    def get_title(self, response):
        return response.xpath("//*[@id=\"main\"]/article/h1/a/text()").extract_first()

    def get_image(self, response):
        image = response.xpath('//*[@id="main"]/article/div/p/img/@src').extract()
        return image