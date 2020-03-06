# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.http.cookies import CookieJar
import json


class HistoriaclinicaSpider(scrapy.Spider):
    name = 'historiaclinica'
    allowed_domains = ['www.intranet.cardioprieto.com']
    start_urls = ['http://www.intranet.cardioprieto.com/index.php/hClinica/index']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'usuario': 'omar', 'pass': 'prieto'},
            callback=self.after_login

        )

    def after_login(self, response):
        pass
