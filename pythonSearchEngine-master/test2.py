#! -*- coding:utf-8 -*-
import sys
from PyDictionary import PyDictionary
try:
    # for Python2
    import Tkinter as tk  ## notice capitalized T in Tkinter
except ImportError:
    # for Python3
    import tkinter as tk  ## notice lowercase 't' in tkinter here
import pandas as pd
import imp
from scipy import spatial
import re, math
from collections import Counter
import warnings
#import the_module_that_warns
warnings.simplefilter("ignore", UserWarning)

imp.reload(sys)
# Load csv
df = pd.read_csv("testexcel.csv")
# df = pd.read_csv("music.csv")
f = open("testexcel.csv", "r")
tf = 0
idf = 0
totalCol = df.shape[0]
allRec = []
WORD = re.compile(r'\w+')
dictionary=PyDictionary()


#convert text to vectors
def text2Vector(text):
    words = WORD.findall(text)
    return Counter(words)

#return cosin similarity for strings
def getCosin(text1, text2):
    vec1 = text2Vector(text1)
    vec2 = text2Vector(text2)
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator




def getLST():
    masterlst = []
    for header in df:
        for item in df[header]:
            masterlst.append(str(item))
    return masterlst




# return cossin similarity of two set, entry values are lists
def getCossinSim(dataSetI, dataSetII):
    return 1 - spatial.distance.cosine(dataSetI, dataSetII)


def getAName(lst):
    temp = []
    for idx in range(len(lst)):
        temp.append(lst[idx])
        idx += 34


##get artist name
def getArtistNameByIndex(idx):
    print("get '{}' at index {}".format(df.at[idx, "artist.name"], idx))
    return df.at[idx, "artist.name"]


# sort by column name
def sort_by(ColName):
    print("sorted by {}".format(ColName))
    return df.sort_values("artist.name", ascending=True)


def getRecordByArtistName(artistName):
    print(df.loc[df['artist.name'] == artistName])
    return df.loc[df['artist.name'] == artistName]


def searching(line, target):
    for word in line.split(' '):
        if word == target:
            print("found " + target)
            return True


def tfidf(term):
    global tf
    count = 0
    df.loc[df['title'] == term]
    print("searching {} words".format(count))
    print("found target {} times".format(tf))


def GroupArtistMbtags():  # grouy by mbtags, get number of mbtags and number of artist/ group by keys
    lst = []
    print("Groupby mbtags\n", df.groupby('artist_mbtags_count').artist_mbtags_count.count())
    print("Groupby keys\n")
    xx = df.groupby('key').key.count()
    for item in xx:
        lst.append(item)
    print(lst)


def getArtistTF(ArtistName):  ##return artist term frequency
    tf = 0
    for i in df['artist.name'] == ArtistName:
        if i == True:
            tf += 1
    print(tf)
    return tf


def getAllTF(term):  ##return TF
    tf = getLST().count(str(term))
    print("term '{}' occurred {} times in the file".format(term, tf))
    return tf


def getSpecificTF(header, term):  # return any tf under specific column
    tf = 0
    for item in df[header]:
        if str(item) == str(term):
            tf += 1
    return tf

def compareCos(query, target):
    return

def getSynonym(term):
    lst = []
    for item in dictionary.synonym(str(term)):
        lst.append(item)
    return lst

def getAdvancedQuery(query):
    advancedQuery = []
    for item in query:
        for subItem in getSynonym(item):
            advancedQuery.append(subItem)
    #print (advancedQuery)
    return advancedQuery

def testRun():
    ##########
    # print(totalCol)
    # getArtistTF('Casual')
    # print(df.loc[df['title'] == 'Relax'])
    # PrintArtistCount()
    # GroupArtistMbtags()
    # dataSetI = [3, 45, 7, 2]
    # dataSetII = [2, 54, 13, 15]
    # print(getCossinSim(dataSetI,dataSetII))
    # print(getAllTF("ccm"))
    # print('Cosine:', getCosin('This sentence is similar to a foo bar sentence .', 'This is a foo bar sentence .'))
    # print(getSynonym("popular"))
    return




# print(a.at[0,"artist.name"])


def removeQueryStopwords(query):  # remove the stop words
    stopwords = ["I", "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as",
                 "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "could",
                 "did", "do", "does", "doing", "down", "during", "each", "few", "for", "from", "further", "had", "has",
                 "have", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him",
                 "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "it",
                 "it's", "its", "itself", "let's", "me", "more", "most", "my", "myself", "nor", "of", "on", "once",
                 "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "she",
                 "she'd", "she'll", "she's", "should", "so", "some", "such", "than", "that", "that's", "the", "their",
                 "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll",
                 "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was",
                 "we", "we'd", "we'll", "we're", "we've", "were", "what", "what's", "when", "when's", "where",
                 "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "would", "you", "you'd",
                 "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves"]
    filteredQuery = [word for word in query.split(" ") if word.lower() not in stopwords]
    # print(filteredQuery)
    return filteredQuery


# class User(object):
#
#     def __init__(self,user_id):
#       if user_id == -1:

#           self.new_user = True
#       else:
#           self.new_user = False
#
#           #fetch all records from db about user_id
#           self._populateUser()
#
#     def commit(self):
#         if self.new_user:
#             #Do INSERTs
#         else:
#             #Do UPDATEs
#
#     def delete(self):
#         if self.new_user == False:
#             return False
#
#         #Delete user code here
#
#     def _populate(self):
#         #Query self.user_id from database and
#         #set all instance variables, e.g.
#         #self.name = row['name']
#
#     def getFullName(self):
#         return self.name


class Window(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # create a prompt, an input box, an output label,
        # and a button to do the computation
        self.prompt = tk.Label(self, text="Search Query:", anchor="w")
        self.entry = tk.Entry(self)
        self.submit = tk.Button(self, text="Search Query", command=self.searchButton)
        self.output = tk.Label(self, text="Def Label")

        self.artistName = tk.Label(self, text="Search artist name:", anchor="w")
        self.artistEntry = tk.Entry(self)
        self.artistSubmit = tk.Button(self, text="Search Artist", command=self.searchArtistButton)
        self.artistOutput = tk.Label(self, text="Def Label")

        # lay the widgets out on the screen.
        self.prompt.pack(side="top", fill="x")
        self.entry.pack(side="top", fill="x", padx=200)
        self.output.pack(side="top", fill="x", expand=True)
        self.submit.pack(side="right")

        self.artistName.pack(side="top", fill="x")
        self.artistEntry.pack(side="top", fill="x", padx=300)
        self.artistOutput.pack(side="top", fill="x", padx=300, expand=True)
        self.artistSubmit.pack(side="right")

    def searchArtistButton(self):
        # get the value from the input widget, convert
        # it to an int, and do a calculation
        try:
            i = str(self.artistEntry.get())
            result = "Your query is: %s \n TF: %s" % (i, getArtistTF(i))
        except ValueError:
            result = "Please enter string only"

        # set the output widget to have our result
        self.artistOutput.configure(text=result)

    def searchButton(self):
        # get the value from the input widget, convert
        # it to an int, and do a calculation
        try:
            i = str(self.entry.get())
            result = "Your query is: %s \n Filtered query is: %s \n Advanced query is: %s" % (i, removeQueryStopwords(i), getAdvancedQuery(removeQueryStopwords(i)))


        except ValueError:
            result = "Please enter string only"

        # set the output widget to have our result
        self.output.configure(text=result)


# if this is run as a program (versus being imported),
# create a root window and an instance of Window,
# then start the event loop
#
if __name__ == "__main__":
    testRun()
    root = tk.Tk()
    Window(root).pack(fill="both", expand=True)
    # uncommon below to run the window
    root.mainloop()

