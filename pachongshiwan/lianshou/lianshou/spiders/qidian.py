# -*- coding: utf-8 -*-
import scrapy

class QidianSpider(scrapy.Spider):
    name = 'qidian'
    allowed_domains = ['www.qidian.com']
    start_urls = ['http://www.qidian.com/all']

    def parse(self, response):
        print(f"response:{response.url}")
    #     book_list = response.xpath("//div[@class='all-book-list']/div/ul/li/div/a/@href")
    #     for url in book_list:
    #         yield scrapy.Request(url=url, callback=self.parse_url, dont_filter=True)
    #     next_urls = response.xpath("//a[@class='lbf-pagination-next']/@href")
    #     try:
    #         for next_url in next_urls:
    #             yield scrapy.Request(url=next_url, callback=self.parse, dont_filter=True)
    #     except Exception as e:
    #         print('已经是最后一页了')
    #
    # def parse_url(self, response):
    #     book_title = response.xpath("//div[@class='book-info ']/h1/em/text()").extract()
    #     book_img = response.xpath("//div[@class='book-img']/a[@id='bookImg']/img/@src").extract()
    #     book_tag = response.xpath("//p[@class='intro']/text()")
    #     book_ticket = response.xpath("//i[@id='recCount']/text()")
    #     book_intro = response.xpath("//div[@class='book-intro']/p/text()")
    #     data = {
    #         'book_title': book_title,
    #         'book_img': book_img,
    #         'book_tag': book_tag,
    #         'book_ticket': book_ticket,
    #         'book_intro': book_intro,
    #     }
    #     print(data)
    #     yield data

