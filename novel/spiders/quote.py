# -*- coding: utf-8 -*-
import scrapy
from novel.items import QuoteItem


class QuoteSpider(scrapy.Spider):
    name = 'quote'
    allowed_domains = ['quote.com']
    start_urls = ['http://quotes.toscrape.com/page/1/']

    def parse(self, response):
        q=QuoteItem()
        for quote in response.css('div.quote'):
            q['text']=quote.css('span.text::text').extract_first()
            q['author']=quote.css('span small::text').extract_first()
            q['tags']=quote.css('div.tags a.tag::text').extract()
            print (q)
            yield q
        next_page=response.css('li.next a::attr(href)').extract_first()
        print (next_page)
        if next_page is not None:
            print ('crawl')
            print(response.follow(next_page,callback=self.parse))
            yield response.follow(next_page,callback=self.parse,dont_filter=True)


