# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem


class TutorialPipeline(object):
    def process_item(self, item, spider):
        try:
            if (item['title'] and item['link'] and item['desc']):
                return item
        except KeyError:
            raise DropItem("Missing field in %s" % item)
