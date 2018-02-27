#! -*- coding:utf-8 -*-

import imp
import sys
imp.reload(sys)
import pandas as pd

# Load csv save as df
df = pd.read_csv("testexcel.csv") 

#print(df.get("artist.name"))


#get artist name
def getArtistNameByIndex (idx):
	print ("get '{}' at index {}".format(df.at[idx,"artist.name"], idx))
	return df.at[idx,"artist.name"]


def getArtistNameByIndex2 (idx):
	print ("get '{}' at index {}".format(df.sort_values(by=["artist.name"]).at[idx,"artist.name"], idx))
	return df.at[idx,"artist.name"]


#sort by column name
def sort_by (ColName):
	print("sorted by {}".format(ColName))
	return df.sort_values(by=[ColName])


def getRecordByArtistName (artistName):
	print(df.loc[df['artist.name'] == artistName])
	return df.loc[df['artist.name'] == artistName]


def searching (line, target):
	for word in line.split(' '):
		if word == target:
			print ("found "+ target)
			return True	

def runcode ():
	count = 0
	found = 0
	for line in f.readlines():
		searching (line, "was")
		if searching (line, "was") == True:
			found += 1
		for word in line:
			count += 1
	print ("searching {} words".format(count))
	print ("found target {} times".format(found))

def testRun():
	print(df.at[0,"artist.name"])
	#getArtistNameByIndex(0)
	#print(sort_by("artist.name"))
	#print(sort_by("artist.name").at[0,"artist.name"])
	getArtistNameByIndex2(0)
	#print(sort_by("artist.name").at[0,"artist.name"])
	


testRun()

#runcode()
