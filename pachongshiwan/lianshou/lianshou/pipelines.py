# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from lianshou.db.models1 import synchronous, LingShiGood_Nav, LingShiGoods, LingShiGoods_Image, LingShiGoods_Details, \
    LingShiGoods_Property
import datetime
from lianshou.items import ChiDe_GoodsItem, ChiDe_Goods_PropertyItem, ChiDe_Good_NavItem, \
    ChiDe_goods_imageItem, ChiDe_goods_detailsItem

(minst, session) = synchronous()


class LianshouPipeline(object):
    def process_item(self, item, spider):
        try:
            # if isinstance(item, LianshouItem):
            #     xiaoshuo = XiaoShuo(book_title=item['book_title'], book_img=item['book_img'], book_tag=item['book_tag'],
            #                         book_ticket=item['book_ticket'], book_Author=item['book_Author'],
            #                         book_type=item['book_type'],book_Author_img=item['book_Author_img'])
            #     minst.add_records(session, xiaoshuo)
            # return item
            if isinstance(item, ChiDe_GoodsItem):
                goods = LingShiGoods(cate_id=item['GoodsItem_cate_id'], goods_name=item['GoodsItem_goods_name'],
                                     detail_url=item["GoodsItem_datail_url"])
                minst.add_records(session, goods)
            if isinstance(item, ChiDe_Goods_PropertyItem):
                proper = LingShiGoods_Property(name=item["name"], value=item["Value"],
                                               detail_url=item["PropertyItem_datail_url"],
                                               create_time=datetime.datetime.now().strftime('%Y-%m-%d'))
                minst.add_records(session, proper)
            if isinstance(item, ChiDe_Good_NavItem):
                good_nav = LingShiGood_Nav(parent_id=item["pid"], cate_name=item["cate_name"]
                                           , sub_name=item["sub_name"], level=item['lelvel']
                                           , cate_id=item["Good_NavItem_cate_id"],
                                           is_delete='0'
                                           )
                print(good_nav.cate_id)
                minst.add_records(session, good_nav)
            if isinstance(item, ChiDe_goods_imageItem):
                img = LingShiGoods_Image(detail_url=item["datail_url"], big_img=item["img_Big"],
                                         small_img=item["img_small"], is_delete='0',
                                         create_time=datetime.datetime.now().strftime('%Y-%m-%d')
                                         )
                minst.add_records(session, img)
            if isinstance(item, ChiDe_goods_detailsItem):
                details = LingShiGoods_Details(detail_url=item["detailsItem_details_url"],
                                               old_price=item["goods_old_price"],
                                               new_price=item["goods_new_price"],
                                               good_number=item["goods_numbering"],
                                               good_state='1',
                                               is_delete='0',
                                               create_time=datetime.datetime.now().strftime('%Y-%m-%d')
                                               )
                minst.add_records(session, details)

        except Exception as e:
            print(f"LianshouPipeline:process_item has error: {e}")
            # return item
        finally:
            return item
