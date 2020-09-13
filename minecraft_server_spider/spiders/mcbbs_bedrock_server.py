# -*- coding: utf-8 -*-
import scrapy

from minecraft_server_spider.items import McbbsBedrockServerItem

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
        tbodies = response.xpath("//table[@id='threadlisttableid']/tbody[starts-with(@id, 'normalthread_')]")
        for tbody in tbodies:
            link = tbody.xpath("./tr/th[@class!='lock']/a[@class='s xst']/@href").extract_first()
            if link:
                yield scrapy.Request(self.base_url + link, callback=self.parse_server)

        # 下一页
        next_page_link = response.xpath(
            "//div[@class='bm bw0 pgs cl']/span[@id='fd_page_bottom']/div/a[@class='nxt']/@href").extract_first()

        # 判断是否还有下一页
        if next_page_link:
            yield scrapy.Request(self.base_url + next_page_link, callback=self.parse)
            # pass

    # 解析服务器详细信息
    def parse_server(self, response):
        server = McbbsBedrockServerItem()

        # 宣传贴标题
        title = response.xpath("//span[@id='thread_subject']/text()").extract_first()
        if title:
            server['title'] = title

        # 发帖人ID
        author = response.xpath(
            "//table[@class='plhin']//div[@class='pls favatar']//div[@class='authi']/a/text()").extract_first()
        if author:
            server['author'] = author

        # 摘取服务器详细信息
        tbody = response.xpath("//table[@class='cgtl mbm']/tbody")
        # 服务器名称
        server['name'] = tbody.xpath("./tr[1]/td/text()").extract_first()
        # 有效状态
        server['valid_status'] = tbody.xpath("./tr[2]/td/text()").extract_first()
        # 游戏模式
        server['game_mode'] = tbody.xpath("./tr[3]/td/text()").extract_first()
        # 支持版本
        server['support_version'] = tbody.xpath("./tr[4]/td/text()").extract_first()
        # 网络类型
        server['network_type'] = tbody.xpath("./tr[5]/td/text()").extract_first()
        # 服务器类型
        server['server_type'] = tbody.xpath("./tr[6]/td/text()").extract_first()
        # 最大在线人数
        server['max_online_num'] = tbody.xpath("./tr[7]/td/text()").extract_first()
        # 插件/行为包
        server['plugins_and_behavior_pack'] = tbody.xpath("./tr[8]/td/text()").extract_first()
        # 联系方式
        server['contact'] = tbody.xpath("./tr[9]/td/text()").extract_first()
        # 服务器IP/域名
        server['ip_or_domain'] = tbody.xpath("./tr[10]/td/text()").extract_first()
        # 服务器端口
        server['port'] = tbody.xpath("./tr[11]/td/text()").extract_first()


        # # 评分人数
        # rate_num = response.xpath("//table[@class='ratl']/tbody[1]/tr/th[1]/a/span/text()").extract_first()
        # if rate_num:
        #     server['rate_num'] = rate_num
        # # 人气
        # popularity = response.xpath("//table[@class='ratl']/tbody[1]/tr/th[2]/i/span/text()").extract_first()
        # if popularity:
        #     server['popularity'] = popularity
        # #金粒
        # gold_nugget = response.xpath("//table[@class='ratl']/tbody[1]/tr/th[3]/i/span/text()").extract_first()
        # if gold_nugget:
        #     server['gold_nugget'] = gold_nugget

        # 永久链接
        permanent_link = response.xpath("//td[@class='plc plm']/div/div/input[@class='px']/@value").extract_first()
        if permanent_link:
            server['permanent_link'] = permanent_link
            server['_id'] = permanent_link.replace('https://www.mcbbs.net/thread-', '').replace('-1-1.html', '')

        yield server