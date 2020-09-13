# -*- coding: utf-8 -*-
import scrapy

from minecraft_server_spider.settings import ITEM_PIPELINES

class McbbsBedrockServerSpider(scrapy.Spider):
    name = 'mcbbs_bedrock_server'
    allowed_domains = ['mcbbs.net']
    start_urls = ['https://www.mcbbs.net/forum-peserver-1.html']
    base_url = 'https://www.mcbbs.net/'
    custom_settings = {
        'ITEM_PIPELINES': {'minecraft_server_spider.pipelines.McbbsBedrockServerPipeline': 300}
    }

    def parse(self, response):
        # 找出具体服务器的宣传贴链接
        tbodies = response.xpath("//table[@id='threadlisttableid']/tbody")
        for tbody in tbodies:
            link = tbody.xpath("./tr/th/a[@class='s xst']/@href").extract_first()
            if link:
                yield scrapy.Request(self.base_url + link, callback=self.parse_server)

        # 下一页
        next_page_link = response.xpath(
            "//div[@class='bm bw0 pgs cl']/span[@id='fd_page_bottom']/div/a[@class='nxt']/@href").extract_first()

        # 判断是否还有下一页
        if next_page_link:
            yield scrapy.Request(self.base_url + next_page_link, callback=self.parse)

    # 解析服务器详细信息
    def parse_server(self, response):
        pass