# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from gaokao.items import GaokaoItem


class UniversitySpider(scrapy.Spider):
    name = 'university'
    allowed_domains = ['gaokao.chsi.com.cn']
    start_urls = ['http://gaokao.chsi.com.cn']

    # 确定要爬取的网址
    def start_requests(self):
        base_url = 'https://gaokao.chsi.com.cn/sch/search.do?searchType=1&start='
        for page in range(138):
            start_num = page * 20
            url = base_url + str(start_num)
            yield Request(url=url, callback=self.parse)

    # 解析内容
    def parse(self, response):
        # 这个不知怎么的，用Xpath会爬不出来，这个是我先用css一个一个选节点测试的。
        # 可以先用requests和Beautifulsoup输出Beautifulsoup解析后的网址，
        # 来确定需要的节点，来帮助爬取。我是这么做的の，从而爬到了需要的信息。
        lists = response.css('.yxk-table .ch-table tr')
        for i in range(1, len(lists)):
            li = lists[i]
            item = GaokaoItem()
            item['name'] = li.css('td a::text')[0].extract().strip()
            item['location'] = li.css('td')[1].xpath('text()').extract()[0].strip()  # 可以用css和Xpath回混合。
            item['affiliate'] = li.css('td')[2].xpath('text()').extract()[0].strip()
            item['types'] = li.css('td')[3].xpath('text()').extract()[0].strip()
            item['level'] = li.css('td')[4].xpath('text()').extract()[0].strip()
            item['satisfication'] = li.css('td a::text')[1].extract().strip()
            yield item
