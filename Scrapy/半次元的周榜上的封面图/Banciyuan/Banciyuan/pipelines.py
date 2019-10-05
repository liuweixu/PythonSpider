# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline


class BanciyuanPipeline(ImagesPipeline):
    # def process_item(self, item, spider):
    #     return item
    def file_path(self, request, response=None, info=None):
        file_name = request.meta['meta']['id'] + ".jpg"
        # print(file_name)
        return file_name

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise scrapy.DropItem('Image Download Failed')
        return item

    def get_media_requests(self, item, info):
        # print(item['cover'])
        yield scrapy.Request(item['cover'], meta={'meta': item})
