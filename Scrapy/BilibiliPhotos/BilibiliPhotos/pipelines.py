# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request


# class BilibiliphotosPipeline(object):
#     def process_item(self, item, spider):
#         return item

class BilibiliphotosPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        item = request.meta['meta']
        file_name = item['title'] + "/" + item['img'].split("/")[-1]
        return file_name

    def get_media_requests(self, item, info):
        return Request(url=item['img'], meta={'meta': item})
