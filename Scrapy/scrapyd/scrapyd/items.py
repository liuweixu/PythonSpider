# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapydItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Title = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    text = scrapy.Field()
    tag = scrapy.Field()
    image = scrapy.Field()
