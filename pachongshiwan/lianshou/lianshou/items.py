# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import datetime
from scrapy.loader.processors import MapCompose, TakeFirst, Join


def remove_slash(value):
    # 去除掉工作城市中的斜杠
    return value.replace(r"\n", "")


def remove_slash1(value):
    return value.replace(" ", "")


def remove_slas(value):
    # 去除掉工作城市中的斜杠
    return value.replace(r"\t", "")




class ChiDe_GoodsItem(scrapy.Item):
    '''
    商品主表
    '''
    GoodsItem_datail_url = scrapy.Field()
    GoodsItem_cate_id = scrapy.Field()
    GoodsItem_goods_name = scrapy.Field()

    def get_name(self):
        return ChiDe_GoodsItem.__name__


class ChiDe_Good_NavItem(scrapy.Item):
    '''
    商品分类表
    '''
    pid = scrapy.Field()
    cate_name = scrapy.Field()
    sub_name = scrapy.Field()
    lelvel = scrapy.Field()
    Good_NavItem_cate_id = scrapy.Field()
    create_time = datetime.datetime.now().strftime('%Y-%m-%d')


    def get_name(self):
        return ChiDe_Good_NavItem.__name__


class ChiDe_goods_imageItem(scrapy.Item):
    '''
        商品图片
    '''

    img_Big = scrapy.Field()
    img_small = scrapy.Field()
    datail_url = scrapy.Field()

    def get_name(self):
        return ChiDe_goods_imageItem.__name__


class ChiDe_goods_detailsItem(scrapy.Item):
    '''
        商品详细页
    '''
    detailsItem_details_url = scrapy.Field()
    goods_numbering = scrapy.Field()
    goods_old_price = scrapy.Field()
    goods_new_price = scrapy.Field()
    good_stock = scrapy.Field()
    create_time = datetime.datetime.now().strftime('%Y-%m-%d')

    def get_name(self):
        return ChiDe_goods_detailsItem.__name__


class ChiDe_Goods_PropertyItem(scrapy.Item):
    '''
        存贮不能分开的商品参数的名字
        '''
    name = scrapy.Field()
    Value = scrapy.Field()
    PropertyItem_datail_url = scrapy.Field()

    def get_name(self):
        return ChiDe_Goods_PropertyItem.__name__


