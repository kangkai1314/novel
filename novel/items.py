# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NovelItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    chapter_name=scrapy.Field()
    chapter_content=scrapy.Field()


class NovelPicItem(scrapy.Item):

    img_name=scrapy.Field()
    img_url=scrapy.Field()
    author=scrapy.Field()
    chapter=scrapy.Field()

class QuoteItem(scrapy.Item):
    text=scrapy.Field()
    author=scrapy.Field()
    tags=scrapy.Field()


class GithubItem(scrapy.Item):
    language=scrapy.Field()
    name=scrapy.Field()
    desc=scrapy.Field()

class JiPiaoItem(scrapy.Item):
    price=scrapy.Field()
    date=scrapy.Field()
    title=scrapy.Field()



