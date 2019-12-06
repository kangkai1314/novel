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
    def process_item(self,item,spider):
        print(item['title'])
        with open('jiPiao.txt','w') as f:
            f.write(item['title'][0].encode('utf-8'))
            for i in item['price']:
                f.write(i.encode('utf-8'))
        return item


from scrapy.pipelines.images import ImagesPipeline
import pymongo
class NovelPicPipeLine(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield Request(item['img_url'])

import redis

from scrapy import signals
import json
import codecs
from collections import OrderedDict

class JsonWithEncodingPipeline(object):
    def __init__(self):
        self.file = codecs.open('data_utf8.json', 'w', encoding='utf-8')

    def process_items(self,item,spider):
        line=json.dumps(OrderedDict(item),ensure_ascii=True,sort_keys=False)+"\n"
        self.file.write(line)
        return item

    def close_spider(self,spider):
        self.file.close()

from scrapy.utils import log
class RedisPipelin(object):

    def __init__(self):
        try:
            self.r=redis.StrictRedis(host='localhost',port=6739)
        except Exception as e:
            raise  Exception('redis connect  failed')

    def process_item(self,item,spider):
        if not item['id']:
            print('no id item')

        str_recorded_item = self.r.get(item['id'])
        final_item = None
        if str_recorded_item is None:
            final_item = item
        else:
            ritem = eval(self.r.get(item['id']))
            if ritem == item:
                log.logger.debug('item ' + item['id'] + ' equal')
            else:
                # info('item '+item['id']+' merge\n'+str(item)+'\n'+str(ritem))
                log.logger.info('item ' + item['id'] + ' use new item')
            # final_item = dict(item.items() + ritem.items())
            final_item = item
        self.r.set(item['id'], final_item)




from scrapy.conf import settings
class MongoPipeLine(object):
    def __init__(self):
        host=settings['MONGODB_HOST']
        port=settings['MONGODB_PORT']
        dbname=settings['MONGODB_DB']
        client=pymongo.MongoClient(host=host,port=port)
        db=client[dbname]



