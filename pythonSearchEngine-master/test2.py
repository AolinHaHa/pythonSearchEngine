#! -*- coding:utf-8 -*-

import imp
import sys
imp.reload(sys)
#sys.setdefaultencoding('utf8')

# f = open("testdata.txt","r")
# print (f)


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


#runcode()
