# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MinecraftserverspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class mcbbsServerItem(scrapy.Item):
    # 服务器名称
    name = scrapy.Field()
    # 有效状态
    valid_status = scrapy.Field()
    # 支持版本
    support_version = scrapy.Field()
    # 盈利模式
    profit_mode = scrapy.Field()
    # 游戏模式
    game_mode = scrapy.Field()
    # 网络类型
    network_type = scrapy.Field()
    # 主机类型
    host_type = scrapy.Field()
    # 正版验证
    online_mode_verification = scrapy.Field()
    # 最大在线人数
    max_online_num = scrapy.Field()
    # 服务器类型
    server_type = scrapy.Field()
    # 服务器Mod/插件
    mods_and_plugins = scrapy.Field()
    # 客户端下载地址
    client_download_link = scrapy.Field()
    # 有无白名单
    whitelist = scrapy.Field()
    # 联系方式
    contact = scrapy.Field()
    # 服务器IP/域名
    ip_or_domain = scrapy.Field()

    