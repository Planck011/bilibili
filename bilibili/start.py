from scrapy import cmdline

cmdline.execute("scrapy crawl bilibili_spider -s JOBDIR=job_info/001".split())