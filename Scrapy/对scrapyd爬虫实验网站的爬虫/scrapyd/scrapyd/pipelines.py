# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os


class ScrapydPipeline(object):
    def process_item(self, item, spider):
        try:
            path = "Scrapyd_Dir"
            if not os.path.exists(path):
                os.makedirs(path)
            text = item['text']
            tag = item['tag']
            title = item['title']
            image = item['image']
            subpath = path + "/{}".format(title)
            if not os.path.exists(subpath):
                os.makedirs(subpath)
            # if len(image) > 0:
            #     for im in image:
            #         with open("./" + subpath, "a") as f:
            #             f.write(image)
            with open("./" + subpath + "/{}.txt".format(title), "w", encoding="utf-8") as f:
                f.write(text + "\n")
                f.write(",".join(tag) + "\n")
                f.write("---------结束-----------\n")
        except:
            pass
        return item
