# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import os
import scrapy


# class MmonlyPipeline(object):
#     def process_item(self, item, spider):
#         return item

class MmonlyPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        path = request.meta['meta']['title']
        filename = path + "/" + request.meta['meta']['img'].split('/')[-1]
        return filename

    def get_media_requests(self, item, info):
        yield scrapy.Request(url=item['img'], meta={'meta': item})
