# -*- coding: utf-8 -*-
import scrapy
from novel.items import GithubItem

class TestspiderSpider(scrapy.Spider):
    name = 'testSpider'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/']

    def parse(self, response):
        pass

