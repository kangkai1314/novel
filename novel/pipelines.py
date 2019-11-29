# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from scrapy.http import Request

class NovelPipeline(object):
    def process_item(self, item, spider):
        currPath='D:\\scrapyprojects\\download\\novel\\quanshuwang'
        temPath=str(item['name'])
        targetPath=currPath+os.path.sep+temPath
        if not os.path.exists(targetPath):
            os.makedirs(targetPath)
        file_name_path=targetPath+os.path.sep+str(item['chapter_name'])+'.txt'
        with open(file_name_path,'w') as f:
            f.write(item['chapter_content']+"\n")
        return item


class JiPiaoPipeLines(object):
    def process_items(self,item,spider):
        with open('jiPiao.txt','a') as f:
            f.write(item['title'])
        return item


from scrapy.pipelines.images import ImagesPipeline
import pymongo
class NovelPicPipeLine(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield Request(item['img_url'])


from scrapy.conf import settings
class MongoPipeLine(object):
    def __init__(self):
        host=settings['MONGODB_HOST']
        port=settings['MONGODB_PORT']
        dbname=settings['MONGODB_DB']
        client=pymongo.MongoClient(host=host,port=port)
        db=client[dbname]



