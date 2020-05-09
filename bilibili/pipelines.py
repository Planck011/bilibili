# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import os
import pymysql
class BilibiliPipeline(object):
    def __init__(self):
        # if os.path.exists('bilili2.csv'):
        #     self.f = open('bilili2.csv', 'a', encoding='utf-8', newline='')
        #     self.w = csv.writer(self.f)
        # else:
        #     self.f = open('bilili2.csv', 'a', encoding='utf-8', newline='')
        #     self.w = csv.writer(self.f)
        #     self.w.writerow(['标题', '分类', 'bv号', 'av号', '播放量', '弹幕数', '最高全站日排行', '点赞', "硬币", "收藏", "分享", 'up主', '标签', '时长', '日期'])
        self.con = pymysql.connect('localhost', 'root', '758144', 'ipproxy', charset='utf8')#连接mysql数据库
        self.cursor = self.con.cursor()


    def process_item(self,item,spider):
        # self.w.writerow([item['title'], item['tname'],item['bvidnum'], item['aid'], item['view'], item['danmu'], item['his_rank'],item['like'], item['coin'], item['favorite'], item['share'], item['name'], item['dynamic'], item['time'], item['date']])
        #存入csv文件
        # return item
        sql = '''INSERT INTO `ipproxy`.`1`(`标题`,`分类`,`bv号`,`av号`,`播放量`,`弹幕数`,`最高全站日排行`,`点赞`, `硬币`, `收藏`, `分享`,`up主`,`标签`,`时长`,`日期`) VALUES (%s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'''
        value = (item['title'], item['tname'],item['bvidnum'], item['aid'],item['view'],item['danmu'],item['his_rank'],item['like'], item['coin'], item['favorite'], item['share'], item['name'], item['dynamic'], item['time'], item['date'])
        self.cursor.execute(sql, value)
        self.con.commit()
    #存入数据库
    def spider_close(self, spider):
        # print('ok')
        # self.f.close()
        self.cursor.close()
        self.conn.close()
