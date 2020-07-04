#导入模块
import requests
from lxml import etree
import time

#新建文件
with open('top250_movie.csv','w',encoding='utf-8') as f:
	f.write('{},{},{},{},{},{}\n'.format('name','score','person','info','year','sentence'))

	for i in range(10):
		url='https://movie.douban.com/top250?start={}'.format(i*25)
		kv={'user-agent':'Mozilla/5.0'}
		r=requests.get(url,headers=kv)
		html=r.text
		s=etree.HTML(html)
		print('打印第{}页'.format(i+1))
		time.sleep(2)

		file = s.xpath('//*[@id="content"]/div/div[1]/ol/li') #整本书

		for div in file:
			name = div.xpath('./div/div[2]/div[1]/a/span[1]/text()')[0] #书名
			score = div.xpath('./div/div[2]/div[2]/div/span[2]/text()')[0] #评分
			person = div.xpath('./div/div[2]/div[2]/div/span[4]/text()')[0] #评价人数
			info = div.xpath('./div/div[2]/div[2]/p[1]/text()')[0].strip() #详细信息
			year = div.xpath('./div/div[2]/div[2]/p[1]/text()')[1].strip() 
			scr = div.xpath('./div/div[2]/div[2]/p[2]/span/text()')#一句话描述

			if len(scr) > 0:
				f.write('{},{},{},{},{},{}\n'.format(name,score,person,info,year,scr[0]))
			else:
				f.write('{},{},{},{},{},{}\n'.format(name,score,person,info,year,'NA'))
