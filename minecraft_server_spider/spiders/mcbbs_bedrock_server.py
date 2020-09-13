# -*- coding: utf-8 -*-
import scrapy

from minecraft_server_spider.settings import ITEM_PIPELINES

class McbbsBedrockServerSpider(scrapy.Spider):
    name = 'mcbbs_bedrock_server'
    allowed_domains = ['mcbbs.net']
    start_urls = ['http://mcbbs.net/']
    base_url = 'https://www.mcbbs.net/'
    custom_settings = {
        ITEM_PIPELINES: {'minecraft_server_spider.pipelines.McbbsBedrockServerPipeline': 300}
    }

    def parse(self, response):
        pass
