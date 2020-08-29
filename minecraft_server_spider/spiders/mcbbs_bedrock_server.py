# -*- coding: utf-8 -*-
import scrapy


class McbbsBedrockServerSpider(scrapy.Spider):
    name = 'mcbbs_bedrock_server'
    allowed_domains = ['mcbbs.net']
    start_urls = ['http://mcbbs.net/']

    def parse(self, response):
        pass
