# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os

class JipinPipeline(object):
    def process_item(self, item, spider):
        try:
            path = "Jipinjiading"
            if not os.path.exists(path):
                os.makedirs(path)
            text = item['text']
            title = item['title']
            print(len(title))
            with open("./" + path + "/{}.txt".format(title), "w", encoding="utf-8") as f:
                f.write(text)
        except:
            pass
        return item