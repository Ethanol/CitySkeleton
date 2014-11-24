#!/usr/bin/python
#coding=utf-8

#from bs4 import BeautifulSoup
import urllib2
import re
import time

fileU=open('Site.txt')
urlStr=fileU.read()
fileU.close()
spUrl=urlStr.split('\n')
class line:
	def __init__(self):
		self.id=-1
		self.name=''
		self.station=[]
spLine=[]
for i in range(0,len(spUrl)-1):
	ThisLine=line()
	tempstr=str(spUrl[i]).split('|')
	ThisLine.id=tempstr[0]
	ThisLine.name=tempstr[1]+'|'+tempstr[2]
	ThisLine.station=tempstr[3].split('@')
#	fileT=open('test.txt','w')
#	fileT.write(str(ThisLine.station))
#	fileT.close()
	print ThisLine.name
	print ThisLine.station[1]
	ThisLine.station.remove('')
	spLine.append(ThisLine)
	print 'spUrl', i
#for i in range(0,len(spLine)):
#	print spLine[i].id, spLine[i].name, spLine[i].station
class p_station:
	def __init__(self):
	#	self.id=-1
		self.name=''
		self.line=[]
		self.count=0
StationPair=[]
StationSet=[]
for i in range(0,len(spLine)):
	i1=0
	i2=0
	for j in range(0,len(spLine[i].station)-1):
		StationStr=spLine[i].station[j]+'%'+spLine[i].station[j+1]
		if StationStr in StationSet:
			This=StationPair[StationSet.index(StationStr)]
			This.line.append(spLine[i].name)
			This.count+=1
			i1+=1
		else:
			ThisPair=p_station()
			ThisPair.name=StationStr
			ThisPair.line.append(spLine[i].name)
			ThisPair.count+=1
			StationPair.append(ThisPair)
			StationSet.append(StationStr)
			i2+=1
	print 'spLine', i, spLine[i].name, len(StationPair), 'New=',i2,'Added=',i1
fileP=open('StationPair.txt','a')
for i in range(0,len(StationPair)):
	fileP.write(StationPair[i].name+'@'+str(StationPair[i].count)+'@')
	for j in range(0,len(StationPair[i].line)):
		fileP.write(StationPair[i].line[j]+'~')
	fileP.write('\n')
	print 'station', i
fileP.close()
