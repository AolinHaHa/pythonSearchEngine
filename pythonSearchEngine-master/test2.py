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


def getAName(lst):
	temp = []
	for idx in range(len(lst)):
		temp.append(lst[idx])
		idx +=34


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
	print ("searching {} words".format(count))
	print ("found target {} times".format(TF))

def GroupArtistMbtags(): #grouy by mbtags, get number of mbtags and number of artist/ group by keys
	lst = []
	print("Groupby mbtags\n",df.groupby('artist_mbtags_count').artist_mbtags_count.count())
	print("Groupby keys\n")
	xx = df.groupby('key').key.count()
	for item in xx:
		lst.append(item)
	print (lst)



def getArtistTF(ArtistName): ##return artist term frequency
	tf = 0
	for i in df['artist.name'] == ArtistName :
		if i == True:
			tf += 1
	print (tf)
	return tf

def getGeneralTF ():
	return




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
	getArtistTF('Casual')
	# print(a.at[0,"artist.name"])


def removeQueryStopwords(query):#remove the stop words
	stopwords = [ "I", "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "could", "did", "do", "does", "doing", "down", "during", "each", "few", "for", "from", "further", "had", "has", "have", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "it", "it's", "its", "itself", "let's", "me", "more", "most", "my", "myself", "nor", "of", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "she", "she'd", "she'll", "she's", "should", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "we", "we'd", "we'll", "we're", "we've", "were", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "would", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves" ]
	filteredQuery = [word for word in query.split(" ") if word.lower() not in stopwords]
	# print(filteredQuery)
	return filteredQuery

