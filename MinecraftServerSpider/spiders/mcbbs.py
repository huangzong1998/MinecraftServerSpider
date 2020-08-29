# -*- coding: utf-8 -*-
import scrapy
from MinecraftServerSpider.items import mcbbsServerItem

class McbbsSpider(scrapy.Spider):
    name = 'mcbbs'
    allowed_domains = ['mcbbs.net']
    start_urls = ['https://www.mcbbs.net/forum-server-1.html']
    base_url = 'https://www.mcbbs.net/'

    # 解析服务器列表页面
    def parse(self, response):
        # 找出所有服务器的宣传贴链接
        tbodies = response.xpath("//table[@id='threadlisttableid']/tbody")
        for tbody in tbodies:
            link = tbody.xpath("./tr/th/a[@class='s xst']/@href").extract_first()
            if link:
                yield scrapy.Request(self.base_url+link, callback=self.parse_server)

        # 找下一页的链接
        # next_page_link = response.xpath("//div[@class='bm bw0 pgs cl']/span[@id='fd_page_bottom']/div/a[@class='nxt']/@href").extract_first()
        # 判断是否还有下一页
        # if next_page_link:
            # yield scrapy.Request(self.base_url+next_page_link, callback=self.parse)

    # 解析服务器详细信息
    def parse_server(self, response):
        # 摘取服务器详细信息
        tr_list = response.xpath("//table[@class='cgtl mbm']/tbody/tr")
        server = mcbbsServerItem()
        for tr in tr_list:
            key = tr.xpath("./th/text()").extract_first()
            value = tr.xpath("./td")
            if key == "服务器名称":
                server['name'] = value.xpath("./text()").extract_first()
            elif key == "有效状态":
                server['valid_status'] = value.xpath("./text()").extract_first()
            elif key == "支持版本":
                server['support_version'] = value.xpath("./text()").extract_first().split()
            elif key == "盈利模式":
                server['profit_mode'] = value.xpath("./text()").extract_first()
            elif key == "游戏模式":
                server['game_mode'] = value.xpath("./text()").extract_first()
            elif key == "网络类型":
                server['network_type'] = value.xpath("./text()").extract_first()
            elif key == "主机类型":
                server['host_type'] = value.xpath("./text()").extract_first()
            elif key == "正版验证":
                server['online_mode_verification'] = value.xpath("./text()").extract_first()
            elif key == "最大在线人数":
                server['max_online_num'] = value.xpath("./text()").extract_first()
            elif key == "服务器类型":
                server['server_type'] = value.xpath("./text()").extract_first()
            elif key == "服务器Mod/插件":
                server['mods_and_plugins'] = value.xpath("./text()").extract_first()
            elif key == "客户端下载地址":
                server['client_download_link'] = value.xpath("./a/text()").extract_first()
            elif key == "有无白名单":
                server['whitelist'] = value.xpath("./text()").extract_first()
            elif key == "联系方式":
                server['contact'] = value.xpath("./text()").extract_first()
            elif key == "服务器IP/域名":
                server['ip_or_domain'] = value.xpath("./a/text()").extract_first()

        yield server
