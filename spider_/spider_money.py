import csv
import os
import time

from lxml import etree
from requests import request


def spider_data(url):
    print("--->开始爬取：", url)
    resp = request("get", url)
    html = resp.content.decode()

    et = etree.HTML(html)
    # 全部条目  //tr[@style]
    infos = et.xpath('//tr[@style]')
    # print(infos)
    data = {}
    for info in infos:
        # 项目代码
        data['p_code'] = info.xpath('./td[1]/text()')[0]
        # 项目名称 //tr[@style]/td[@class='fname']/a/text()
        data['p_name'] = info.xpath('./td[@class="fname"]/a/text()')[0]
        # 万份收益
        data['earning'] = info.xpath('./td[@class="numblack"]/span[@class="fb"]/text()')[0]
        # 日期
        data['start_date'] = info.xpath('./td[5]/text()')[0]
        # 7日年化
        data['earn_7d'] = info.xpath('./td[@class="numblack"][3]/text()')[0]
        # 14日年化
        data['earn_14d'] = info.xpath('./td[@class="numblack"][4]/text()')[0]
        # 28日年化
        data['earn_28d'] = info.xpath('./td[@class="numblack"][5]/text()')[0]
        # 35日年化
        data['earn_35d'] = info.xpath('./td[@class="numblack"][6]/text()')[0]
        # 近一月
        data['path_1m'] = info.xpath('./td[@class="numred"][1]/text()')[0]
        # 近3月
        data['path_3m'] = info.xpath('./td[@class="numred"][2]/text()')[0]
        # 近6月
        data['path_6m'] = info.xpath('./td[@class="numred"][3]/text()')[0]
        # 近1年
        data['path_1y'] = info.xpath('./td[@class="numred"][4]/text()')[0]
        # 起购金额
        data['start_money'] = info.xpath('./td[@class="td_fl"]/div[@class="rate_f"]/div[starts-with(@class, "r")]/text()')[0]

        print(data)
        pipeline(data)


def pipeline(data):
    # 处理data中的起步金额
    money = data['start_money']
    # print(money)
    money1 = money.split('元')[0]
    if '万' in money:
        money1 = int(money.split('万')[0]) * 10000
    data['start_money'] = money1

    # 将数据存储到本地csv文件
    has_header = os.path.exists('spider_money.csv')

    with open('spider_money.csv', 'a') as f:
        writer = csv.DictWriter(f, fieldnames=data.keys())
        if not has_header:
            writer.writeheader()
        writer.writerow(data)

    pass


if __name__ == '__main__':

    # url = 'http://fund.eastmoney.com/trade/hb.html'
    url = 'http://fund.eastmoney.com/trade/hb.html'
    spider_data(url)

    print("__OVER__")
