# -*- coding: utf-8 -*-

"""
    
    私密代理使用示例
   接口鉴权说明：
   目前支持的鉴权方式有 "simple" 和 "hmacsha1" 两种，默认使用 "simple"鉴权。
   所有方法均可添加关键字参数sign_type修改鉴权方式。
"""

import kdl
import re
import time




# 获取ip白名单, 返回ip列表
# ip_whitelist = client.get_ip_whitelist()
# print("ip whitelist", ip_whitelist)

# 设置ip白名单，参数类型为字符串或列表或元组
# 成功则返回True, 否则抛出异常
# client.set_ip_whitelist([])
# client.set_ip_whitelist("171.113.244.40,171.113.244.41")
# print(client.get_ip_whitelist())



# client.set_ip_whitelist(tuple())

# 提取私密代理ip, 第一个参数为提取的数量, 其他参数以关键字参数的形式传入(不需要传入signature和timestamp)
# 具体有哪些参数请参考帮助中心: "https://www.kuaidaili.com/doc/api/getdps/"
# 返回ip列表
# 注意：若您使用的是python2, 且在终端调用，或在文件中调用且没有加 "# -*- coding: utf-8 -*-" 的话
# 传入area参数时，请传入unicode类型，如 area=u'北京,上海'

def getIP(num):
    ips = client.get_dps(num, format='json')
    # ips = ['182.40.253.44:18076', '60.167.112.98:23358']
    print("dps proxy: ", ips)
    f = open(r'C:\Users\pyh1343122828\PycharmProjects\bilibili\bilibili\nlist.txt', 'a')
    for i in range(len(ips)):
        ip = 'http://' + str(ips[i]) + '\n'
        f.write(ip)
    f.close()

def checkIP():
    f = open(r'C:\Users\pyh1343122828\PycharmProjects\bilibili\bilibili\nlist.txt', 'r')
    lines = f.readlines()
    f_w = open(r'C:\Users\pyh1343122828\PycharmProjects\bilibili\bilibili\nlist.txt', 'w')
    count = 0
    cc = 0
    for line in lines:
        parts = re.match('(\w+://)([^:]+?:[^@]+?@)?(.+)', line.strip())
        # print(parts.group(3))
        ip = parts.group(3)
        valids = client.check_dps_valid(ip)
        seconds = client.get_dps_valid_time(ip)
        print("seconds: ", seconds)
        flag = str(list(valids.values())[0])
        aa = 'False'
        if flag == aa:
            count = count+1
            continue
        else:
            cc = cc+1
        f_w.write(line)
    print("删除:", count)
    print("剩余:", cc)
    return cc
    f.close()
    f_w.close()

# 检测私密代理有效性： 返回 ip: true/false 组成的dict
# ips = client.get_dps(2, sign_type='simple', format='json')

# 获取私密代理剩余时间: 返回 ip: seconds(剩余秒数) 组成的dict
# ips = client.get_dps(5, format='json')
# seconds = client.get_dps_valid_time(ips)
# print("seconds: ", seconds)
if __name__ == '__main__':
    auth = kdl.Auth("978821290983857", "f93p3rkf8h84e9z9ylw8ls91e9f398b2")
    client = kdl.Client(auth)

    # 获取订单到期时间, 返回时间字符串
    checkIP()
    getIP(140)
    # expire_time = client.get_order_expire_time()
    # print("expire time", expire_time)
    # 获取计数版ip余额（仅私密代理计数版）
    # while True:
    #     a = checkIP()
    #     # getIP(100)
    #     if a < 60:
    #         getIP(60)
    #     balance = client.get_ip_balance(sign_type='hmacsha1')
    #     print("余额: ", balance)
    #     time.sleep(600)
    # proxyauthorization = client.get_proxy_authorization(plain_text=1,sign_type='simple')
    #     # print("proxyauthorization: ", proxyauthorization)
    balance = client.get_ip_balance(sign_type='hmacsha1')
    print("余额: ", balance)

# 获取代理鉴权信息
# 获取指定订单访问代理IP的鉴权信息。
# 鉴权信息包含用户名密码，用于请求私密代理/独享代理/隧道代理时进行身份验证。
# plain_text 为1 表示明文显示用户名和密码
# 具体请看：https://www.kuaidaili.com/doc/api/getproxyauthorization/
# proxyauthorization = client.get_proxy_authorization(plain_text=1,sign_type='simple')
# print("proxyauthorization: ", proxyauthorization)

