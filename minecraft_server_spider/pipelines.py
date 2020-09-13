# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import datetime
import re

import pymongo

class MinecraftServerSpiderPipeline(object):
    def process_item(self, item, spider):
        return item

class McbbsJavaServerPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client['MinecraftServers']
        self.collection=self.db['McbbsJavaServer']

    def process_item(self, item, spider):
        # 数据清洗

        # 服务器名称
        name = item['name']
        if name:
            item['name'] = name.replace('\t', '')

        # 有效状态
        valid_status = item['valid_status']
        if valid_status:
            item['valid_status'] = valid_status.replace('\t', '')

        # 支持版本
        support_version = item['support_version']
        if support_version:
            item['support_version'] = support_version.split()

        # Mod/插件
        mods_and_plugins = item['mods_and_plugins']
        if mods_and_plugins:
            item['mods_and_plugins'] = re.sub('[+=#$%&,，|、/◆〓-]', ' ', mods_and_plugins).split()

        # # 人气
        # popularity = item['popularity']
        # if popularity:
        #     item['popularity'] = popularity.replace('+', '')
        #
        # # 金粒
        # gold_nugget = item['gold_nugget']
        # if gold_nugget:
        #     item['gold_nugget'] = gold_nugget.replace('+', '')

        # 设置更新日期
        utcTime = datetime.datetime.now() - datetime.timedelta(hours=8)
        item['update_date'] = utcTime
        # 将数据保存到数据库
        self.collection.save(dict(item))
        # 向控制台输出元数据
        return item

    def close_spider(self, spider):
        self.client.close()

class McbbsBedrockServerPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client['MinecraftServers']
        self.collection=self.db['McbbsBedrockServer']

    def process_item(self, item, spider):
        # 服务器名称
        name = item['name']
        if name:
            item['name'] = name.replace('\t', '')

        # 有效状态
        valid_status = item['valid_status']
        if valid_status:
            item['valid_status'] = valid_status.replace('\t', '')

        # 支持版本
        support_version = item['support_version']
        if support_version:
            item['support_version'] = support_version.split()

        # Mod/插件
        plugins_and_behavior_pack = item['plugins_and_behavior_pack']
        if plugins_and_behavior_pack:
            item['plugins_and_behavior_pack'] = re.sub('[+=#$%&,，|、/◆〓-]', ' ', plugins_and_behavior_pack).split()

        # 设置更新日期
        utcTime = datetime.datetime.now() - datetime.timedelta(hours=8)
        item['update_date'] = utcTime
        # 将数据保存到数据库
        self.collection.save(dict(item))
        # 向控制台输出元数据
        return item

    def close_spider(self, spider):
        self.client.close()