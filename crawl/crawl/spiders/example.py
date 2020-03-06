# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['www.intranet.cardioprieto.com']
    start_urls = ['http://www.intranet.cardioprieto.com/']

    def parse(self, response):
        pass
