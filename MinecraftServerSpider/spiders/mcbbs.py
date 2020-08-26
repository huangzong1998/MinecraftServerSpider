# -*- coding: utf-8 -*-
import scrapy


class McbbsSpider(scrapy.Spider):
    name = 'mcbbs'
    allowed_domains = ['mcbbs.net']
    start_urls = ['https://www.mcbbs.net/forum-server-1.html']

    def parse(self, response):
        table = response.xpath("//table[@id='threadlisttableid']").extract()
        print(table)

