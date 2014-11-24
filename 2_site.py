#!/usr/bin/python
#coding=utf-8

from bs4 import BeautifulSoup
import urllib2
import re
import time

fileU=open('LineUrl.txt')
urlStr=fileU.read()
fileU.close()
spUrl=urlStr.split(';')
print spUrl
FileS=open('Site.txt','a')
for i in range(0,len(spUrl)-1):
	if(spUrl[i].find('8684.cn/x_ff2b3e48')>=0):
		print 'find!'
		continue
	name=spUrl[i].split(',')[0]
	Url=spUrl[i].split(',')[1]
	Req = urllib2.Request(Url)
	resp = urllib2.urlopen(Req)
	respHtml = resp.read()
	soup = BeautifulSoup(respHtml,fromEncoding="gb18030")
	Found = soup.findAll(attrs={'class':'hc_p8'})

	for j in range(0,len(Found)):
		Res1=str(Found[j]).split(r'<a href=')
		FileS.write(str(i)+'|'+name+'|'+Res1[0].split('<i>')[1].split('：')[0]+'|')
		for k in range(1,len(Res1)):
			FileS.write(Res1[k].split('>')[1].split('<')[0]+'@')
		FileS.write('\n')
	print i, name
	time.sleep(1)
FileS.close()
