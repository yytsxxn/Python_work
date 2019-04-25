#!/usr/bin/python
#!encoding=utf-8
import requests
import time
import re
import csv
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt

mp.rcParams["font.sans-serif"] = ["SimHei"] 
mp.rcParams["axes.unicode_minus"] = False

#设置URL固定部分
url = 'http://www.cbooo.cn/year?year='
#设置请求头部信息
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
#循环抓取列表页信息
for year in range(2009,2019):
    if year == 2009:
        year = str(year)
        a = (url + year)
        r = requests.get(url = a, headers = headers)
        html = r.content
    else:
        year = str(year)
        a = (url + year)
        r = requests.get(url = a, headers = headers)
        html2 = r.content
        html = html + html2
    #每次间隔0.5秒
    time.sleep(0.5)
lj = BeautifulSoup(html, 'html.parser')
#提取名称、类型、总票房（万）、平均票价、场均人次及国家及地区
result = lj.find_all('td')
mname = []
title = ""
index = 1
year = 2009
for i in result:
    i = str(i)
    title = re.findall(r'</span>(.*?)</p>',i,re.I|re.M)
    if len(title) > 0:
        mname.append(index)
        index = index + 1
        mname.append(title[0])
    else:
        info = re.findall(r'<td>(.*?)</td>',i,re.I|re.M)
        mname.append(info[0])
k = 0
data = []
while k < 2000:
    year = 2009
    year = year + (k // 200)
    data.append([mname[k], mname[k + 1], mname[k + 2], mname[k + 3], mname[k + 4], mname[k + 5], mname[k + 6], mname[k + 7], year, 1])
    k = k + 8
print(len(data))#一共250条数据
#将结果存到data.csv文件中
with open('data.csv', 'w+') as fout:
    cin = csv.writer(fout, lineterminator = '\n')
    #写入row_1    
    cin.writerow(["index", "name", "type", "zpf", "mantimes", "price", "area", "datatime", "year", "mark"])
    for item in data:
        cin.writerow(item)
data1 = pd.read_csv('data.csv', encoding='utf-8')   

#十年间同一类型电影平均票房走势
data = data1
data = data.groupby(['type', 'year']).zpf.mean().unstack()
data.fillna(0, inplace = True) 
plt.figure(figsize = (12, 6))
plt.title('同一类型电影十年间平均票房走势', fontsize = 20)
plt.xlabel('年份')
plt.ylabel('平均票房(万)')
plt.plot(data.T)
data.T.plot()

#十年间同一地区在前25排名中占比的变化趋势
data = data1
#mark设置为1/25，方便后边算比例
data.mark = 0.04
data = data.groupby(['area', 'year']).mark.sum().unstack()
data.fillna(0, inplace = True)
plt.figure(figsize = (12, 6))
plt.title('同一地区十年间在前25排名中占比的变化趋势', fontsize = 20)
plt.xlabel('年份')
plt.ylabel('占比')
plt.plot(data.T)
data.T.plot()

#十年间不同电影类型总票房的变化
data = data1
data = data.groupby(['type', 'year']).zpf.sum().unstack()
data.fillna(0, inplace = True) 
plt.figure(figsize = (12, 6))
plt.title('电影类型在十年间总票房变化', fontsize = 20)
plt.xlabel('年份')
plt.ylabel('总票房（万）')
plt.plot(data.T)
data.T.plot()

#分析影响总票房的因素
data = data1
plt.figure(figsize = (12, 6))
plt.title('总票房和排片场数的关系', fontsize = 20)
plt.xlabel('排片场数（万）')
plt.ylabel('总票房(万)')
plt.scatter(data.zpf, (data.zpf/data.price/data.mantimes), c = 'b')

data = data1
plt.figure(figsize = (12, 6))
plt.title('总票房和场均人次的关系', fontsize = 20)
plt.xlabel('场均人次')
plt.ylabel('总票房（万）')
plt.scatter(data.mantimes, data.zpf, c='g')

data = data1
plt.figure(figsize = (12, 6))
plt.title('总票房和平均票价的关系', fontsize = 20)
plt.xlabel('平均票价')
plt.ylabel('总票房（万）')
plt.scatter(data.price, data.zpf, c='r')
plt.show()