import requests
from lxml import etree
import time

for i in range(10):
	url='https://movie.douban.com/top250?start={}'.format(i*25)
	kv={'user-agent':'Mozilla/5.0'}
	r=requests.get(url,headers=kv)
	html=r.text
	s=etree.HTML(html)
	time.sleep(2)

	file = s.xpath('//*[@id="content"]/div/div[1]/ol/li') #整本书

	for div in file:
		name = div.xpath('./div/div[2]/div[1]/a/span[1]/text()')[0] #书名
		score = div.xpath('./div/div[2]/div[2]/div/span[2]/text()')[0] #评分
		person = div.xpath('./div/div[2]/div[2]/div/span[4]/text()')[0] #评价人数

		print('{},{},{}'.format(name,score,person))
	
