#豆瓣电影单页全部信息
import requests
from lxml import etree
import time

url='https://movie.douban.com/top250'
kv={'user-agent':'Mozilla/5.0'}
r=requests.get(url,headers=kv)
html=r.text
s=etree.HTML(html)

'''
#单个电影的信息爬取
file = s.xpath('//*[@id="content"]/div/div[1]/ol/li[1]') #整本书

for div in file:
	name = div.xpath('./div/div[2]/div[1]/a/span[1]/text()') #书名
	score = div.xpath('./div/div[2]/div[2]/div/span[2]/text()') #评分

	print('{}{}'.format(name,score))
'''
#单页信息爬取
file = s.xpath('//*[@id="content"]/div/div[1]/ol/li') #整本书

for div in file:
	name = div.xpath('./div/div[2]/div[1]/a/span[1]/text()')[0] #书名
	score = div.xpath('./div/div[2]/div[2]/div/span[2]/text()')[0] #评分
	person = div.xpath('./div/div[2]/div[2]/div/span[4]/text()')[0] #评价人数
	info = div.xpath('./div/div[2]/div[2]/p[1]/text()')[0].strip() #详细信息
	year = div.xpath('./div/div[2]/div[2]/p[1]/text()')[1].strip('\n').strip() 
	scr = div.xpath('./div/div[2]/div[2]/p[2]/span/text()')[0]#一句话描述
	print('{},{},{},{},{},{}'.format(name,score,person,info,year,scr))
	
