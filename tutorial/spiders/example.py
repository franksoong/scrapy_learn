# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem
from scrapy.loader import ItemLoader


class ExampleSpider(scrapy.Spider):
    name = 'huxiu'
    allowed_domains = ['huxiu.com']
    start_urls = ['https://www.huxiu.com/']

    def parse(self, response):
        for sel in response.css('div.mod-art'):
            i = ItemLoader(item=TutorialItem(), selector=sel)
            i.add_xpath('title', './/div/h2/a/text()')
            i.add_xpath('link', './/div/h2/a/@href')
            i.add_xpath('desc', ".//div[@class='mob-sub']/text()")
            yield i.load_item()
