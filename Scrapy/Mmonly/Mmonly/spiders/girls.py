# -*- coding: utf-8 -*-
import scrapy
from Mmonly.items import MmonlyItem


class GirlsSpider(scrapy.Spider):
    name = 'girls'
    allowed_domains = ['www.mmonly.cc']
    start_urls = ['http://www.mmonly.cc/ktmh/dmmn/']

    # 爬取页码链接
    def parse(self, response):
        base_url = "http://www.mmonly.cc/ktmh/dmmn/list_29_"
        for page in range(1, 81): # 这个80页是手动统计的，目前可以考虑这个最大页码的统计用编程帮助。
            url = base_url + str(page) + ".html"
            yield scrapy.Request(url, callback=self.parse_page)

    # 爬取每个页面的所有图片链接（转入新的页面）
    def parse_page(self, response):
        hrefs = response.xpath('//*[@id="infinite_scroll"]/div/div[2]/div[1]/span/a/@href').extract()
        for url in hrefs:
            yield scrapy.Request(url, callback=self.parse_detail)

    # 这个放在外面行不通。。。
    # 错误的案例：会只能爬每个图片页的里面的2和更大的页码指向的链接里面的图片，其他爬不出来。emmmmmm。
    # def parse_detail_page(self, response):
    #     parse_urls = []
    #     parse_urls.append(response.url)
    #     urls = response.xpath('/html/body/div[2]/div[2]/div[8]/ul/li/a/@href').extract()[2:-1]
    #     for url in urls:
    #         parse_urls.append(self.start_urls[0] + url)
    #     for parse_url in parse_urls:
    #         yield scrapy.Request(self.start_urls[0] + parse_url, callback=self.parse_detail)

    def parse_detail(self, response):
        img_urls = response.xpath('//*[@id="big-pic"]/p/a/img/@src').extract()
        for img_url in img_urls:
            item = MmonlyItem()
            item['title'] = response.xpath('/html/body/div[2]/div[2]/div[2]/h1/text()').extract_first()
            item['img'] = img_url
            yield item
        # 这个图片里面的页码的爬取，最好在这个parse_detail里面进行更好
        urls = response.xpath('/html/body/div[2]/div[2]/div[8]/ul/li/a/@href').extract()[2:-1]
        for url in urls:
            yield scrapy.Request(self.start_urls[0] + url, callback=self.parse_detail)
