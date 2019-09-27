# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os


# 将爬取到的内容保存到txt文件中，分标题保存。
class FuyanjiPipeline(object):
    def process_item(self, item, spider):
        try:
            path = "Fuyanji_Contents"
            if not os.path.exists(path):
                os.makedirs(path)
            text = item['text']
            title = item['title']
            with open("./" + path + "/{}.txt".format(title), "w", encoding="utf_8") as f:
                f.write(text)
        except:
            pass
        return item
