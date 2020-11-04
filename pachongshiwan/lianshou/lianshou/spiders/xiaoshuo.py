# -*- coding: utf-8 -*-
import scrapy
# from lianshou.items import LianshouItem
from bshead import create_bs_driver
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver

'''
对起点中文网,标签为所有的小说进行爬取,使用response经行数据抓取
'''


class XiaoshuoSpider(scrapy.Spider):
    name = 'xiaoshuo'
    allowed_domains = ['www.qidian.com']
    start_urls = ["http://www.qidian.com/all"]

    def __init__(self):
        scrapy.Spider.__init__(self, self.name)
        self.driver = create_bs_driver()

        self.driver.set_page_load_timeout(50)

    def __del__(self):
        self.driver.quit()

    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield scrapy.Request(url=url, callback=self.parse, meta={'type': 'next'}, dont_filter=True)

    def parse(self, response):
        print(f"response:{response.url}")
        next_url = response.url
        # 1 . http://www.qidian.com/all
        next_r = scrapy.Request(url=next_url, meta={'type': 'next'}, callback=self.parse, dont_filter=True)
        yield next_r

        book_list = response.xpath("//div[@class='all-book-list']/div/ul/li/div/a/@href").extract()
        for urls in book_list:
            url = 'https:' + urls
            yield scrapy.Request(url=url, callback=self.parse_url, dont_filter=True)

    def parse_url(self, response):
        mylist = []
        book_title = response.xpath("//div[@class='book-info ']/h1/em/text()").extract()
        book_img = response.xpath("//div[@class='book-img']/a[@id='bookImg']/img/@src").extract()
        book_tag = response.xpath("//p[@class='intro']/text()").extract()
        book_ticket = response.xpath("//i[@id='recCount']/text()").extract()
        book_Author = response.xpath("/html/body/div[2]/div[6]/div[1]/div[2]/h1/span/a/text()").extract()
        book_Author_img = response.xpath("//*[@id='authorId']/a/img/@src").extract()
        book_types = response.xpath("//p[@class='tag']//a/text()").extract()
        b = ''
        for book in book_types:
            b += book
        mylist.append(b)
        book_type = mylist
        # book_intro = response.xpath("//div[@class='book-intro']/p/text()").extract()
        data = {
            'book_title': book_title if book_title else '信息缺失',
            'book_img': book_img if book_img else '信息缺失',
            'book_tag': book_tag if book_tag else '信息缺失',
            'book_ticket': book_ticket if book_ticket else '信息缺失',
            'book_Author': book_Author if book_Author else '信息缺失',
            'book_type': book_type if book_type else '信息缺失',
            'book_Author_img': book_Author_img if book_Author_img else '信息缺失'
            # 'book_intro': book_intro if book_intro else '信息缺失',
        }
        # print(data)
        item = LianshouItem(book_title=data['book_title'], book_img=data['book_img'], book_tag=data['book_tag'],
                            book_ticket=data['book_ticket'], book_Author=data['book_Author'],
                            book_type=data["book_type"], book_Author_img=data['book_Author_img']
                            )
        yield item
