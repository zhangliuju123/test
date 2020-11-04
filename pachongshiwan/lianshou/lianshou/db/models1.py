# -*- coding: utf-8 -*-


__auto__ = 'zhangliujun'
__date__ = '2019/1/18 14:38'

'''
自定义orm业务模型类
'''

from lianshou.db.mysql_helper import MySQLORMHelper, Base

from sqlalchemy import Column, String, Integer, ForeignKey,Text
import json


class LingShiGood_Nav(Base):
    __tablename__ = "Good_Nav"
    nid = Column(Integer, primary_key=True)
    parent_id = Column(String(20))
    cate_name = Column(String(200))
    sub_name = Column(String(200))
    level = Column(String(20))
    cate_id = Column(String(200))  # 分类的url
    is_delete = Column(String(10))


class LingShiGoods(Base):
    __tablename__ = "Goods"
    goods_id = Column(Integer, primary_key=True)  # db can set it auto_increment
    cate_id = Column(String(20))
    goods_name = Column(String(200))
    detail_url = Column(String(200))


class LingShiGoods_Image(Base):
    __tablename__ = "Image"
    img_id = Column(Integer, primary_key=True)
    detail_url = Column(String(20))
    small_img = Column(Text)
    big_img = Column(Text)
    create_time = Column(String(20))
    is_delete = Column(String(10))


class LingShiGoods_Details(Base):
    __tablename__ = "Goods_Detail"
    detail_id = Column(Integer, primary_key=True)
    detail_url = Column(String(20))
    old_price = Column(String(30))
    new_price = Column(String(30))
    good_number = Column(String(200))
    good_state = Column(String(200))
    good_stock = Column(String(20))
    create_time = Column(String(200))
    is_delete = Column(String(10))


class LingShiGoods_Property(Base):
    __tablename__ = "Good_Property"
    gp_id = Column(Integer, primary_key=True)
    name = Column(String(200))
    value = Column(String(200))
    detail_url = Column(String(200))
    create_time = Column(String(200))




# def __str__(self):
#     res_dict = dict(
#         id=self.id,
#         book_title=self.book_title,
#         image_url=self.image_url,
#     )
#     return json.dumps(res_dict)

# class BookDetail(Base):
#     __tablename__ = "book_detail"
#     id = Column(Integer, primary_key=True)
#     book_url_fprint = Column(String(50), ForeignKey(Book.book_url_fprint))
#     # book_url_fprint = Column(String(50))
#     book_description = Column(Text)

def synchronous():
    minst = MySQLORMHelper()
    session = minst.create_session()
    return (minst, session)

    # print(session)
    #
    # #result = minst.query_conditions(session, Book, Book.id, 21)
    #
    #
    #
    # #minst.update_record(session, Book, Book.id, 21, {Book.book_price:2000})
    #
    # #minst.delete_records(session, Book, Book.id, 22)
    #
    #
    # book_list = []
    # for i in range(10):
    # 	book = Book(book_title = f"book-{i}", image_url=f"image-{i}",
    # 				book_price=random.randint(20, 100), book_url=f"http://www.book-{i}.com")
    # 	book_list.append(book)
    #
    # minst.add_records(session, book_list)


if __name__ == "__main__":
    synchronous()
