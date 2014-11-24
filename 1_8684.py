#!/usr/bin/python

from bs4 import BeautifulSoup
import urllib2
import re
import time

City='chengdu'
CityNumber=8
UrlStr = "http://"+City+".8684.cn/line"
for i in range(1,CityNumber+1):
	Url = UrlStr+str(i)
	time.sleep(1)
	Req = urllib2.Request(Url)
	resp = urllib2.urlopen(Req)
	respHtml = resp.read()
	soup = BeautifulSoup(respHtml,fromEncoding="GB2312")
	if i==1:
		Found = soup.findAll('a',href=re.compile(r"/x_(?!ff2b3e48)"))
	elif i!=4: 
		Found = Found + soup.findAll('a',href=re.compile("/x_(?!ff2b3e48)"))
	print i

print "Res=",Found
class Line:
	def __init__(self):
		self.name=''
		self.link=''
LineSet=[]
p1=re.compile(r"><")
p2=re.compile(r"")
fileH=open('LineUrl.txt','w')
for j in range(0,len(Found)):
	thisStr=str(Found[j])
	thisLine=Line()
	thisLine.name=thisStr.split('>')[1].split('<')[0]
	thisLine.link="http://"+City+".8684.cn"+thisStr[9:20]
	LineSet.append(thisLine)
	print j,LineSet[j].name, LineSet[j].link
	fileH.write(thisLine.name+','+thisLine.link+';')
fileH.close()
