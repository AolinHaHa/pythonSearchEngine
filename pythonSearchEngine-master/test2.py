#! -*- coding:utf-8 -*-

import imp
import sys
imp.reload(sys)
import pandas as pd
import numpy as np

# Load csv

df = pd.read_csv("testexcel.csv") 
f = open("testexcel.csv","r")
tf = 0
idf = 0
totalCol = df.shape[0]
allRec = []
# 	singleRec.append(ii)
# allRec.append(singleRec)

# def getallRec():
# 	global allRec
	# singleRec = []
for i in f:
	for ii in i.split(','):
		allRec.append(ii)
# return allRec
temp = []
for idx in range(len(allRec)):
	temp.append(allRec[idx])
	idx +=34
	
print(temp)


def getAName(lst):
	temp = []
	for idx in range(len(lst)):
		temp.append(lst[idx])
		idx +=34
# 	return temp
# print(getAName(allRec))




#get artist name
def getArtistNameByIndex (idx):
	print ("get '{}' at index {}".format(df.at[idx,"artist.name"], idx))
	return df.at[idx,"artist.name"]

#sort by column name
def sort_by (ColName):
	print("sorted by {}".format(ColName))
	return df.sort_values("artist.name", ascending=True)


def getRecordByArtistName (artistName):
	print(df.loc[df['artist.name'] == artistName])
	return df.loc[df['artist.name'] == artistName]


def searching (line, target):
	for word in line.split(' '):
		if word == target:
			print ("found "+ target)
			return True	
def countTerm(term):
	return

def tfidf (term):
	global tf
	count = 0
	df.loc[df['title'] == term]
	# for line in f.readlines():
	# 	searching (line, "was")
	# 	if searching (line, "was") == True:
	# 		TF += 1
	# 	for word in line:
	# 		count += 1
	print ("searching {} words".format(count))
	print ("found target {} times".format(TF))

def GroupArtistMbtags():
	lst = []
	print(df.groupby('artist_mbtags_count').artist_mbtags_count.count())
	xx = df.groupby('key').key.count()
	for item in xx:
		lst.append(item)
	print (lst)



def PrintArtistCount():
	print(df['artist.name'].value_counts())

def testRun():
	global totalCol
	print(df.at[0,"artist.name"])
	print (tf)
	##########
	#print(df.loc[df['title'] == 'Relax'])
	#PrintArtistCount()
	print(totalCol)
	# GroupArtistMbtags()
	a = sorted ("artist.name")
	# print(a.at[0,"artist.name"])




#testRun()
# for i in df:
# 	for ii in i.split(' ')
