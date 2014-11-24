#!/usr/bin/python
#coding=utf-8

#from bs4 import BeautifulSoup
import urllib2
import re
import time

fileU=open('StationPair.txt')
PairStr=fileU.read()
fileU.close()
Pair=PairStr.split('\n')
class p_station:
	def __init__(self):
		self.start=''
		self.end=''
		num=0
DoP=[]
for i in range(0,len(Pair)-1):
	newp=p_station()
	newp.num=str(Pair[i]).split('@')[1]
	newp.start=str(Pair[i]).split('@')[0].split('%')[0]
	newp.end=str(Pair[i]).split('@')[0].split('%')[1]
	DoP.append(newp)
fileD=open('DoP.txt','w')
fileD.write('source\ttarget\tweight\n')
for i in range(0,len(DoP)):
	fileD.write(DoP[i].start+'\t'+DoP[i].end+'\t'+DoP[i].num+'\n')
fileD.close()
