# -*- coding: utf-8 -*-
import scrapy
import json
from bilibili.items import BilibiliItem
# from scrapy.conf import settings 老版本配置settings
from scrapy.utils.project import get_project_settings
import re
import scrapy_proxies


class BilibiliSpiderSpider(scrapy.Spider):
    settings = get_project_settings()
    name = 'bilibili_spider'
    allowed_domains = ['bilibili.com']
    start_urls = ['https://search.bilibili.com/']
    video_av = range(settings.get("VIDEO_START"), settings.get("VIDEO_END"))
    # video_av = range(10000, 10003)
    def start_requests(self):
        for av in self.video_av:
            print(f'爬取 av{av}')
            yield scrapy.Request(
                url=f'https://search.bilibili.com/all?keyword=av{av}',
                callback=self.parse_page, dont_filter=False
            )

    def parse_page(self, response):
        av = response.xpath(".//span[@class='type avid']/text()").get()
        print(response.request.headers['User-Agent'])
        print(av)
        if av == None:
            return
        try:
            href = response.xpath("/html/body/div[3]/div/div[2]/div/div[1]/div[2]/ul/li[1]/div/div[1]/a/@href").get()
            date = response.xpath("/html/body/div[3]/div/div[2]/div/div[1]/div[2]/ul/li[1]/div/div[3]/span[3]/text()").get()
            date = date.strip()
            # print(href)(/html/body/div[3]/div/div[2]/div/div[1]/div[2]/ul/li[1]/div/div[1]/a)
            # time = response.xpath("/html/body/div[3]/div/div[2]/div/div[1]/div[2]/ul/li/a/div/span[1]/text()").get()
            time = response.xpath("/html/body/div[3]/div/div[2]/div/div[1]/div[2]/ul/li[1]/a/div/span[1]/text()").get()
            # print(time)
            item = BilibiliItem()
            item['time'] = time
            item['date'] = date
            r = re.findall('BV[0-9a-zA-Z]*', href)
            url2 = "https://api.bilibili.com/x/web-interface/view?&bvid=" + "".join(r)
            print(url2)
            yield scrapy.Request(url2, callback=self.parse, dont_filter=True, meta={"item": item})
        except:
            return

    def parse(self, response):
        item = response.request.meta['item']
        json_data = json.loads(response.text)
        json_Info1 = json_data['data']
        item['bvidnum'] = json_Info1['bvid']
        item['aid'] = json_Info1['aid']
        item['tname'] = json_Info1['tname']
        item['title'] = json_Info1['title']
        # item['desc'] = json_Info1['desc']
        own = json_Info1['owner']
        item['name'] = own['name']
        stat = json_Info1['stat']
        item['view'] = stat['view']
        item['danmu'] = stat['danmaku']
        item['reply'] = stat['reply']
        item['favorite'] = stat['favorite']
        item['coin'] = stat['coin']
        item['share'] = stat['share']
        item['like'] = stat['like']
        item['his_rank'] = stat['his_rank']
        item['dynamic'] = json_Info1['dynamic']
        yield item
