# import requests
# from lxml import etree
#
#
# url = "https://search.bilibili.com/all?keyword=av10010&from_source=nav_search&spm_id_from=333.851.b_696e7465726e6174696f6e616c486561646572.9"
#
# # resp = requests.get(url)
# # text = resp.text
# # with open("search.html", 'w',encoding='utf-8') as fp:
# #     fp.write(text)
# parser = etree.HTMLParser(encoding='utf-8')
# html = etree.parse("search.html", parser=parser)
#
# date = html.xpath(".//li[@class='video-item avclass list']/div/div/span[3]/text()")[0]
# date = date.strip()
# print(date)