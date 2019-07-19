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


from scrapy.pipelines.images import ImagesPipeline

class NovelPicPipeLine(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield Request(item['img_url'])



