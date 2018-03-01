#! -*- coding:utf-8 -*-

import imp
import sys
imp.reload(sys)
import pandas as pd

# Load csv save as df
df = pd.read_csv("testexcel.csv") 

tf = 0
idf = 0
#print(df.get("artist.name"))


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


def tfidf ():
	global tf
	count = 0
	for line in f.readlines():
		searching (line, "was")
		if searching (line, "was") == True:
			TF += 1
		for word in line:
			count += 1
	print ("searching {} words".format(count))
	print ("found target {} times".format(TF))


def testRun():
	print(df.at[0,"artist.name"])
	#print(sort_by("artist.name"))
	#getArtistNameByIndex(0)
	#print(df.sort_values("artist.name", ascending=True))
	# print (df.sort_values("artist.name", ascending=True))
	# print (sort_by("artist.name").at[0,"artist.name"])
	# tfidf()
	print (tf)
	


testRun()

#runcode()
