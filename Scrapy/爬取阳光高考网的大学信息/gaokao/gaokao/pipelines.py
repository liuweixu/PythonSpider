# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import openpyxl


class GaokaoPipeline(object):

    # 重新open_spider()库，为了确定要保存的文件的格式
    def open_spider(self, spider):
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.append(['院校名称', '院校所在地', '院校隶属', '院校类型', '学历层次', '满意度'])

    # 保存yield所返回的信息。
    def process_item(self, item, spider):
        line = [item['name'], item['location'], item['affiliate'], item['types'], item['level'], item['satisfication']]
        self.ws.append(line)
        return item

    # 重写close_spider()库，为了确定保存的文件名。
    def close_spider(self, spider):
        self.wb.save('university.xlsx')
