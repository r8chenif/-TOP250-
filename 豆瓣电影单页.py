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
file = s.xpath('//*[@id="content"]/div/div[1]/div/table[1]')

for div in file:
	name = div.xpath('.//tr/td[2]/div[1]/a/text()')[0].strip()
	score = div.xpath('.//tr/td[2]/div[2]/span[2]/text()')[0].strip()
	person = div.xpath('.//tr/td[2]/div[2]/span[3]/text()')[0].strip('(').strip(')').strip()
	info = div.xpath('.//tr/td[2]/p[1]/text()')[0].strip()
	sentence = div.xpath('.//tr/td[2]/p[2]/span/text()')[0].strip()

	print('{},{},{},{},{}'.format(name,score,person,info,sentence))
	
