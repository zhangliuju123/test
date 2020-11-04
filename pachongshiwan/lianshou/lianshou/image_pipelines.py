# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '2018/12/24 下午4:39'

'''
图片下载
'''
import scrapy

from scrapy.pipelines.images import ImagesPipeline


class MysmallImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        img_url = item.get('img_url', None)
        if img_url != None:
            yield scrapy.Request(url=img_url)


class MyBigImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        img_url = item.get('img_url', None)
        if img_url != None:
            yield scrapy.Request(url=img_url)
