# -*- coding: utf-8 -*-
import datetime
import os
import re
import time

__auto__ = 'zhangliujun'
__date__ = '2019/1/15 11:19'

from bshead import create_bs_driver

# url = 'https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=54802https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=54802'
# driver = create_bs_driver()
#
# # zishu = driver.find_elements_by_xpath("/html/body/div[2]/div[6]/div[1]/div[2]/p[3]/em[1]/span")
# # pinfen = driver.find_elements_by_xpath("//*[@id='score1']")
# # paiming = driver.find_elements_by_xpath("//div[@class='ticket rec-ticket']//p[3]/text()")
# # with open("web.html", 'w', encoding="utf8") as f:
# #     f.write(driver.page_source)
# # time.sleep(5)
# # driver.find_elements_by_xpath("//*[@id='s-box']")[0].send_keys('历史')
# # driver.find_elements_by_xpath("//*[@id='search-btn']/em")[0].click()
# # time.sleep(5)
# driver.find_elements_by_xpath("//div[@class='lbf-pagination']/ul/li[9]/a")[0].click()
# print(driver.current_url)

# url = 'http://www.lingshi.com/product/lingshi-13283.htm'
# i = []
# url_str = url.split('-')
# url_str1 = url_str[1].split('.')
# print(url_str1[0])
# i.append(url_str1[0])
# print(i)
# for k in i :
#     k.join(',')
#     print(k)
# print(zishu,type(zishu),pinfen,paiming)

# list1 = ["1", "2", "3"]
# # for i in list1:
# a = ','.join(list1)
# print(a, type(a))
# list2 = []
# b = ''
# # for i in list1:
# #     b += i
# i = str(list1)
# print(type(i))
# # list2.append(b)
# print(b)

# url = 'http://www.lingshi.com/list/f257_o1.htm'
# url1 = url.split('/')[4]
# url2 = url1.split(".")[0]
# url3 = url2.split('_')[0]
# print(url3)

# str1 = '<tr>\n\t\t\t\t\t\t\t<td>毛重: 400克</td>\t\t\t\t\t\t\t<td>种类：啤酒</td>\n\t\t\t\t\t\t\t<td>食用方法：打开即可食用</td>\n\t\t\t\t\t\t</tr>'
# str2 = str1.split()
# print(str2)
# list1 = ['\n\t\t\t\t\t\t\t\t品牌:\n\t\t\t\t\t\t\t\t', '\n\t\t\t\t\t\t\t', '芳草手抓包香草味葵花籽*250g 约9袋', '\n\t\t\t\t\t\t\t\t口 味：', '\xa0\xa0\xa0产 地：', '\t\t\t\t\t\t\t']
# for i in list1:
#     i=i.strip()
#     if i:
#         print(i)
# list2 = []
# list3 = []
# list4 = []
# list1 = ['\n\t\t\t\t\t\t', '\n\t\t\t\t\t\t\t', '\n\t\t\t\t\t\t\t\t品牌:\n\t\t\t\t\t\t\t\t', '苏太太', '\n\t\t\t\t\t\t\t', '\n\t\t\
# t\t\t\t\t', '苏太太醉食尚花生原味*260g 约5袋', '\n\t\t\t\t\t\t\t', '\n\t\t\t\t\t\t\t\t口 味：', '原味', '\xa0\xa0\xa0产 地：', '江苏',
#          '\t\t\t\t\t\t\t', '\n\t\t\t\t\t\t', '\n\t\t\t\t\t\t', '\n\t\t\t\t\t\t\t', '毛重: 260克', '\t\t\t\t\t\t\t',
#          '种类：花生', '\n\t\t\t\t\t\t\t', '食用方法：打开即可食用', '\n\t\t\t\t\t\t', '\n\t\t\t\t\t\t', '\n\t\t\t\t\t\t\t',
#          '生产日期：2017-08', '\t\t\t\t\t\t\t', '保质期：8个月', '\t\t\t\t\t\t\t', '储存方法：请置于阴凉干燥处，避光保存。', '\t\t\t\t\t\t',
#          '\n\t\t\t\t\t']
#
# for i in list1:
#     if i:
#         if "：" in i:
#             k = i.strip().split("：")
#             for j in k:
#                 if j != '':
#                     list2.append(j)
#         else:
#             k = i.strip().split(":")
#             for j in k:
#                 if j != '':
#                     list2.append(j)
# del list2[2]
# del list2[2]
# print(list2)
# print("______")
# for l in list2:
#     if list2.index(l) % 2 == 0:
#         list3.append(l)
#     else:
#         list4.append(l)
# print(list3)
# print('_______')
# print(list4)
# list4 = []
# list3 = ['生产日期：2018-11', '保质期：9个月', '储存方法：请置于阴凉干燥处，避光保存。']
# for i in list3:
#     k = i.split('：')
#     for j in k:
#         list4.append(j)
# print(list4)
#     if i:
#         k = i.strip().split("：")
#         for j in k:
#             if j != '':
#                 list2.append(j)
# print(list2)


# for i in list1:
#     list2 = i.split(':')
#     print(i)
# print(list2)
# for k in list2:
#     k.split(':')
#     print(k)
# print(len(i))
# print(i)
# print("************")


# i = i.strip()
# list1 = ['\n\t\t\t\t\t\t\t\t品牌:\n\t\t\t\t\t\t\t\t', '\n\t\t\t\t\t\t\t', '芳草手抓包香草味葵花籽*250g 约9袋', '\n\t\t\t\t\t\t\t\t口 味：', '\xa0\xa0\xa0产 地：', '\t\t\t\t\t\t\t', '毛重: 250克', '种类：瓜子', '食用方法：打开即可食用', '生产日期：2018-11', '保质期：9个月', '储存方法：请置于阴凉干燥处，避光保存。']
# for i in list1:
#     i.strip()
#     if i :
#         print(i)
# url = ['http://www.lingshi.com/product/lingshi-1168.htm'][0]
# url1 = url
# url_str = url1.split('-')
# url_str1 = url_str[1].split('.')
# print(url_str1[0])
# img = ['http://image.lingshi.com/newimages/01/0101/01010019/detail/b1.jpg',
#        'http://image.lingshi.com/newimages/headline/show.jpg',
#        'http://image.lingshi.com/newimages/01/0101/01010019/detail/b2.jpg',
#        'http://image.lingshi.com/newimages/01/0101/01010019/detail/b3.jpg',
#        'http://image.lingshi.com/newimages/01/0101/01010019/detail/b4.jpg',
#        ' http://image.lingshi.com/newimages/headline/Package.jpg',
#        'http://image.lingshi.com/newimages/01/0101/01010019/detail/b5.jpg']
# k = ','.join(img)
# print(k,type(k))
# list1 = ['a', 'b', 'c']
# for i in range(len(list1)):
#     print(i)
# t = datetime.datetime.now().strftime('%Y-%m-%d')
#
# print(t, type(t))
# url1 = ['http://www.lingshi.com/list/?catid=53']
# url1 = url1[0].split('/')
# url2 = url1[4].split(".")[0]
# url3 = url2.split('=')[1]
# class_url = url3
# print(class_url)

# generator_ex = (x * x for x in range(10))
# for i in generator_ex:
#     print(i)
# import re
#
# print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.match('com', 'www.runoob.com'))  # 不在起始位置匹配
# line = "Cats are smarter than dogs"
#
# matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
#
# if matchObj:
#     print("matchObj.group() : ", matchObj.group())
#     print("matchObj.group() : ", matchObj.group(1))
#     print("matchObj.group() : ", matchObj.group(2))
#
# else:
#     print("No match!!")
# def create_pwd_md5(str_password, type="sha1"):
#     import hashlib
#     h1 = hashlib.md5() if type == "md5" else hashlib.sha1()
#     h1.update(str_password.encode(encoding="utf-8"))
#     return h1.hexdigest()
#
#
# def func1(url):
#     return url
#
#
# def func2(url):
#     return url
#
#
# math_jpg_pattern = {
#     'newimages': func1,
#     'images': func2,
# }
#
# list1 = [['http://image.lingshi.com/images/201712/source_img/12339_a1.jpg',
#           'http://image.lingshi.com/images/201712/source_img/12339_a3.jpg',
#           'http://image.lingshi.com/images/201712/source_img/12339_a4.jpg',
#           'http://image.lingshi.com/images/201712/source_img/12339_a5.jpg',
#           'http://image.lingshi.com/images/201712/source_img/12339_a7.jpg'],
#          ['http://image.lingshi.com/newimages/09/0901/09010437/detail/b.jpg']]
# list2 = []
# list3 = []
# for i in list1[0]:
#     y = create_pwd_md5(i)
#     img_url = '/static/images/' + y + '.jpg'
#     list2.append(img_url)
#     j = ','.join(list2)
# print(f'list1[0]={j}')
# for i in list1[1]:
#     y = create_pwd_md5(i)
#     img_url = '/static/images/' + y + '.jpg'
#     list3.append(img_url)
#     j = ','.join(list3)
# print(f'list1[1]={j}')
# for i in list1:
#     for j in i:
#         if 'images' in j:
#             y = create_pwd_md5(j)
#             img_url = '/static/images/' + y + '.jpg'
#             list2.append(img_url)
#             k1 = ','.join(list2)
#         if 'newimages'in j:
#             y = create_pwd_md5(j)
#             img_url = '/static/images/' + y + '.jpg'
#             list3.append(img_url)
#             k2 = ','.join(list3)
#
# print(f'list2={k1}')
# print(f'list3={k2}')
#
# print(os.path)

s = 'hello world'
k = s.center(30)
l = '     hello world     '
print('<' + k + '>')
print(','.join(s))
print(s.split(' '))
print(l.strip())
print(os.path)
nestedList = [[1, 2, 3], [3, 4, 5], [6, 7, 8]]


def enumList(nestedList):
    for subList in nestedList:
        for element in subList:
            yield element


for num in enumList(nestedList):
    print(num)
numList = list(enumList(nestedList))
print(numList)

m = re.match('hello', 'hello')
if m is not None:
    print(m.group())
print(m.__class__.__name__)
import sys

print(sys.path)

