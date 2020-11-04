# -*- coding: utf-8 -*-
import scrapy
from lianshou.items import ChiDe_Goods_PropertyItem, ChiDe_GoodsItem, ChiDe_Good_NavItem, ChiDe_goods_imageItem, \
    ChiDe_goods_detailsItem


def create_pwd_md5(str_password, type="sha1"):
    import hashlib
    h1 = hashlib.md5() if type == "md5" else hashlib.sha1()
    h1.update(str_password.encode(encoding="utf-8"))
    return h1.hexdigest()


class ChideSpider(scrapy.Spider):
    name = 'chide'
    allowed_domains = ['www.lingshi.com']
    start_urls = ['http://www.lingshi.com/']

    def parse(self, response):
        self.count = 0  # 3
        names = response.xpath("//div[@class='menu_list']")[2:-3]  # 一级菜单名
        for name in names:  # 遍历一级菜单名
            name_p = name.xpath('./h3/a/text()').extract()[0]
            names_list = name.xpath("./div/ul/li")  # 二级菜单名
            self.count += 1
            a = self.count
            num = 1
            for name1 in names_list:
                name_s = name1.xpath("./a/text()").extract()[0]  # 二级菜单名
                box_list = name1.xpath("./a/@href").extract()  # 二级菜单分类地址
                for url in box_list:
                    '''
                    处理url,取url中的数字作为关联字段
                    '''
                    url1 = url.split('/')[4]
                    url2 = url1.split(".")[0]
                    url3 = url2.split('_')[0]
                    url4 = url3.split("f")[1]
                    class_url = url4

                    self.count += 1  # 3 4 5
                    r = scrapy.Request(url=url, callback=self.parse_url, dont_filter=True)
                    yield r

                    '''
                    获取分类表信息
                    '''
                    if num == 1:

                        item = ChiDe_Good_NavItem(cate_name=name_p, lelvel='1', sub_name='', pid=0,
                                                  Good_NavItem_cate_id=class_url)
                    else:
                        item = ChiDe_Good_NavItem(cate_name=name_p, lelvel='2', pid=a, sub_name=name_s,
                                                  Good_NavItem_cate_id=class_url)
                    num += 1
                    yield item

    def parse_url(self, response):
        '''
        生产出详情页的url
        :param response:
        :return:
        '''
        details_urls = response.xpath("//div[@class='snack_wrap fixed']/ul//li/a/@href").extract()
        for url in details_urls:
            r = scrapy.Request(url=url, callback=self.parse_details, dont_filter=True)
            yield r

    def parse_details(self, response):
        '''
        解析详情页
        :param response:
        :return:
        '''
        '''
                处理详情页url,将详情页url中的数字作为关联字段
                '''
        '''
                                               获取goods表的信息
                                               '''
        url1 = response.url
        url_str = url1.split('-')
        url_str1 = url_str[1].split('.')
        GoodsItem_cate_id = response.xpath("//div[@class='crumbs mt10']//a[3]/@href").extract()
        url1 = GoodsItem_cate_id[0].split('/')
        url2 = url1[4].split(".")[0]
        url3 = url2.split('=')[1]
        class_url = url3
        if class_url == '53':
            print(53)
        name = response.xpath("//h3[@class='name']/text()").extract()[0]
        item1 = ChiDe_GoodsItem(GoodsItem_goods_name=name, GoodsItem_datail_url=url_str1[0],
                                GoodsItem_cate_id=class_url)
        yield item1
        img_dict = {'small': '', 'big': ''}
        img_list = []
        big_list = []
        small_list = []
        img_Big = response.xpath("//p[@style='text-align: center;']//img/@src").extract()  # 获取商品图片,并且分类
        if img_Big:
            img_list.append(img_Big)
            img_Bigs = ','.join(img_Big)
            i = create_pwd_md5(img_Bigs)
            img_smalls = response.xpath("//div[@class='list_img']//a/@href").extract()
            img_list.append(img_smalls)
            for i in img_list:
                for j in i:
                    if 'images' in j:
                        y = create_pwd_md5(j)
                        img_url = '/static/images/' + y + '.jpg'
                        big_list.append(img_url)
                        k1 = ','.join(big_list)
                        img_dict['small'] = k1
                    if 'newimages' in j:
                        y = create_pwd_md5(j)
                        img_url = '/static/images/' + y + '.jpg'
                        small_list.append(img_url)
                        k2 = ','.join(small_list)
                        img_dict['big'] = k2
                img_small = ','.join(img_smalls)
                y = create_pwd_md5(img_small)
            url = response.url
            url_str = url.split('-')
            url_str1 = url_str[1].split('.')
            img_item = ChiDe_goods_imageItem(img_small=img_dict['small'], img_Big=img_dict['big'],
                                             datail_url=url_str1[0])
            yield img_item
        else:
            imgs_Big = response.xpath("//div[@class='tabCot_pro']/table//p//img/@src").extract()
            if imgs_Big:
                img_list.append(img_Big)
                img_Big_str = ','.join(imgs_Big)
                i = create_pwd_md5(img_Big_str)
                img_smalls = response.xpath("//div[@class='list_img']//a/@href").extract()
                img_list.append(img_smalls)
                for i in img_list:
                    for j in i:
                        if 'images' in j:
                            y = create_pwd_md5(j)
                            img_url = '/static/images/' + y + '.jpg'
                            big_list.append(img_url)
                            k1 = ','.join(big_list)
                            img_dict['small'] = k1
                        if 'newimages' in j:
                            y = create_pwd_md5(j)
                            img_url = '/static/images/' + y + '.jpg'
                            small_list.append(img_url)
                            k2 = ','.join(small_list)
                            img_dict['big'] = k2
                img_small = ','.join(img_smalls)
                y = create_pwd_md5(img_small)
                url = response.url
                url_str = url.split('-')
                url_str1 = url_str[1].split('.')
                img_item = ChiDe_goods_imageItem(img_small=img_dict['small'], img_Big=img_dict['big'],
                                                 datail_url=url_str1[0])
                yield img_item
            else:
                img_Big = response.xpath("//div[@id='tabCot_0']/table//img/@src").extract()
                img_list.append(img_Big)
                img_smalls = response.xpath("//div[@class='list_img']//a/@href").extract()
                img_list.append(img_smalls)
                for i in img_list:
                    for j in i:
                        if 'images' in j:
                            y = create_pwd_md5(j)
                            img_url = '/static/images/' + y + '.jpg'
                            big_list.append(img_url)
                            k1 = ','.join(big_list)
                            img_dict['small'] = k1
                        if 'newimages' in j:
                            y = create_pwd_md5(j)
                            img_url = '/static/images/' + y + '.jpg'
                            small_list.append(img_url)
                            k2 = ','.join(small_list)
                            img_dict['big'] = k2
                    img_small = ','.join(img_smalls)
                    y = create_pwd_md5(img_small)
                url = response.url
                url_str = url.split('-')
                url_str1 = url_str[1].split('.')
                img_item = ChiDe_goods_imageItem(img_small=img_dict['small'], img_Big=img_dict['big'],
                                                 datail_url=url_str1[0])
                yield img_item
        """
        获取详情表信息
        """
        goods_numbering = response.xpath("//p[@class='num']/em/text()").extract()  # 商品编号
        goods_old_price = response.xpath("//li[@id='price2']/p/text()").extract_first()[5:-1]
        goods_new_price = response.xpath("//span[@id='shopprice']/text()").extract()
        details_url = url_str1
        good_itme = ChiDe_goods_detailsItem(goods_numbering=goods_numbering, goods_old_price=goods_old_price,
                                            goods_new_price=goods_new_price, detailsItem_details_url=details_url[0],
                                            good_stock='1',
                                            )
        yield good_itme
        """
        获取商品参数
        """
        names_list = response.xpath("//div[@id='lingshi_a']/table//text()").extract()
        list2 = []
        list3 = []
        list4 = []
        for i in names_list:
            if i:
                if "：" in i:
                    k = i.strip().split("：")
                    for j in k:
                        if j != '':
                            list2.append(j)
                else:
                    k = i.strip().split(":")
                    for j in k:
                        if j != '':
                            list2.append(j)
        del list2[2]
        for l in list2:
            if list2.index(l) % 2 == 0:
                list3.append(l)
            else:
                list4.append(l)
        for i in range(len(list3)):
            name = list3[i]
            value = list4[i]
            item = ChiDe_Goods_PropertyItem(name=name, Value=value, PropertyItem_datail_url=url_str1[0])
            yield item
