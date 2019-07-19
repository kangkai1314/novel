# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from novel.items import NovelPicItem


class NovelcrawlerSpider(scrapy.Spider):
    name = 'novelcrawler'
    allowed_domains = ['quanshuwang.com']
    start_urls = ['http://www.quanshuwang.com/list/1_2.html',
        'http://www.quanshuwang.com/list/1_3.html',
        'http://www.quanshuwang.com/list/1_4.html',
        'http://www.quanshuwang.com/list/1_5.html',
        'http://www.quanshuwang.com/list/1_6.html',
        'http://www.quanshuwang.com/list/1_7.html',
        'http://www.quanshuwang.com/list/1_8.html',
        'http://www.quanshuwang.com/list/1_9.html',
        'http://www.quanshuwang.com/list/1_10.html',]



    def parse(self, response):
        urls=response.xpath('//*[@id="navList"]/section/ul')
        n = NovelPicItem()
        for url in urls:
            print (url)
            img_name=url.xpath('//li/a/img/@alt').extract_first()
            img_url=url.xpath('//li/a/img/@src').extract_first()
            author=url.xpath('//li/span/a[2]/text()').extract_first()
            n['img_name'] = img_name
            n['img_url'] = img_url.encode('utf-8')
            n['author'] = author.encode('utf-8')
            print (n)

            with open('a.txt','a') as f:
                f.write(img_name.encode('utf-8'))
                f.write(author.encode('utf-8'))
            read_url=url.xpath('//li/a[@class="l mr10"]/@href').extract_first()
            print (read_url)
            print (Request(read_url,callback=self.parse_read))
            yield Request(read_url,callback=self.parse_read)

    def parse_read(self,response):
        print ('crawl url ')
        next_url=response.xpath('//*[@id="container"]/div[2]/section/div/div[1]/div[2]/a[1]/@href').extract_first()
        print ('next_url')
        print (next_url)
        yield  Request(url=next_url,callback=self.parse_chapter)

    def parse_chapter(self,response):
        n = NovelPicItem()
        all=response.xpath('//div[@class="clearfix dirconone"]/li/a/text()').extract()
        for a in all:
            print (a)
            c_name=a
            n['chapter']=c_name
            print (c_name)
            with open('a.txt','a') as f:
                f.write(c_name.encode('utf-8')+'\n')

            yield n








