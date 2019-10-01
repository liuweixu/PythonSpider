# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy


class BingPipeline(ImagesPipeline):
    # def process_item(self, item, spider):
    #     return item

    # 用来确定图片的文件名。
    def file_path(self, request, response=None, info=None):
        # 由于标题过长，会分成自动分成两半，前面的部作为文件夹的名字，后面的部分作为图片的名字。
        # 所以，我们有必要进行删除一些不必要的名字的部分，可以发现，这些标题基本是在后面有一个括号，我们可以删去
        # 这些无关紧要的括号就行。
        file_name = request.meta['meta']['title'].split("(")[0] + ".png"
        return file_name

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise scrapy.DropItem('Image Download Failed')
        return item

    def get_media_requests(self, item, info):
        yield scrapy.Request(url=item['url'], meta={'meta': item})
