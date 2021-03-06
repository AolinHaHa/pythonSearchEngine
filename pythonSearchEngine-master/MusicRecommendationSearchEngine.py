#! -*- coding:utf-8 -*-
import sys
from PyDictionary import PyDictionary
import itertools
from operator import itemgetter
import pandas as pd
import imp
from scipy import spatial
import re, math, json
from collections import Counter
from lxml import html
import requests
from time import sleep
import warnings
try:
    # for Python2
    import Tkinter as tk  ## notice capitalized T in Tkinter
    from Tkinter import *
except ImportError:
    # for Python3
    import tkinter as tk  ## notice lowercase 't' in tkinter here
    from tkinter import *


# import the_module_that_warns
warnings.simplefilter("ignore", UserWarning)
imp.reload(sys)
# Load csv
df = pd.read_csv("music.csv")
# df = pd.read_csv("music.csv")
# f = open("testexcel.csv", "r")
tf = 0
idf = 0
totalCol = df.shape[0] - 1
allRec = []
WORD = re.compile(r'\w+')
dictionary = PyDictionary()

# load music review data, store into dictionary data type
reviewData = []
# with open('test_music.json') as f:
with open('reviews_Digital_Music_5.json') as f:
    for line in f:
        # reviewData.append(json.loads(line)['reviewText'])
        record = {json.loads(line)['asin']: json.loads(line)['reviewText']}
        reviewData.append(dict(record))


# print(reviewData)


# convert text to vectors
def text2Vector(text):
    words = WORD.findall(re.sub("[^a-zA-Z]",  # Search for all non-letters
                          " ",          # Replace all non-letters with spaces
                          str(text)))
    return Counter(words)


# return cosin similarity for strings
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


# find everything in dataframe
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


# returtn tfidf
def tfidf(tf, idf):
    # print("searching {} words".format(count))
    # print("found target {} times".format(tf))
    tfidf = tf * idf
    print("tfidf is: ", str(tfidf))
    return tfidf


# grouy by mbtags, get number of mbtags and number of artist/ group by keys
def GroupArtistMbtags():
    lst = []
    print("Groupby mbtags\n", df.groupby('artist_mbtags_count').artist_mbtags_count.count())
    print("Groupby keys\n")
    xx = df.groupby('key').key.count()
    for item in xx:
        lst.append(item)
    print(lst)


##return artist term frequency
def getArtistTF(ArtistName):
    tf = 0
    for i in df['artist.name'] == ArtistName:
        if i == True:
            tf += 1
    print(tf)
    return tf


# return idf
def getIdf(tfk):
    # print("totalCol: ", totalCol)
    # print("tfk: ", tfk)
    try:
        return math.log((totalCol / tfk), 2)
    except ZeroDivisionError:
        return 0


##return TF
def getAllTF(term):
    tf = getLST().count(str(term))
    print("term '{}' occurred {} times in the file".format(term, tf))
    return tf


# return any tf under specific column
def getSpecificTF(header, term):
    tf = 0
    for item in df[header]:
        if str(item) == str(term):
            tf += 1
    return tf


# return a list of synonymn words
def getSynonym(term):
    lst = []
    lst.append(str(term))
    for item in dictionary.synonym(str(term)):
        lst.append(item)
    return lst


def getAdvancedQuery(query):
    advancedQuery = []
    # for item in query.split(' '):
    for item in query:
        for subItem in getSynonym(item):
            advancedQuery.append(subItem)

    return " ".join(advancedQuery)


def getAllArtist():
    artistLst = []
    for i in df['artist.name']:
        artistLst.append(i)
    return artistLst


def getAllTitle():
    titleLst = []
    for i in df['title']:
        titleLst.append(i)
    return titleLst


# return a list of cosine similarity value of all review data and query
def getMaxReviewCosSim(query):
    scores = []
    for target in reviewData:
        record = {'id': str(target.keys())[12:-3], 'cosSim': getCosin(str(target.values()), query)}
        scores.append(dict(record))
    # print(scores)
    return scores


##return a list of dicts with key=title name, value = cosin similarity
def getMaxTitleCosSim(query):
    scores = []
    for target in getAllTitle():
        record = {'Title': target, 'cosSim': getCosin(target, query)}
        scores.append(dict(record))
    # print(scores)
    scores = sorted(scores, key=itemgetter('cosSim'))
    scores.reverse()
    return scores


##return a list of dicts with key=title name, value = cosin similarity
def getMaxArtistCosSim(query):
    scores = []
    for target in getAllArtist():
        record = {'ArtistName': target, 'cosSim': getCosin(target, query)}
        scores.append(dict(record))
    # print(scores)
    scores = sorted(scores, key=itemgetter('cosSim'))
    scores.reverse()
    print(scores)
    return scores


# groupby the getMaxCossim result by music ID, and get the average similarity score
def rankingResult(iniResult):
    lst = []
    rankingLst = []
    iniResult = sorted(iniResult, key=itemgetter('id'))
    for key, value in itertools.groupby(iniResult, key=itemgetter('id')):
        for i in value:
            lst.append(i.get('cosSim'))
        avgscore = float(sum(lst) / len(lst))
        rankingLst.append([key, avgscore])
    rankingLst = sorted(rankingLst, key=itemgetter(1))
    rankingLst.reverse()
    print(rankingLst)
    print("length rangking list: ", str(len(rankingLst)))

    return rankingLst


# remove the stop words
def removeQueryStopwords(query):
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


AsinList = []
SongNames = []


def AmzonParser(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
    page = requests.get(url, headers=headers)
    while True:
        sleep(3)
        try:
            doc = html.fromstring(page.content)
            XPATH_NAME = '//h1[@id="title"]//text()'
            XPATH_SALE_PRICE = '//span[contains(@id,"ourprice") or contains(@id,"saleprice")]/text()'
            XPATH_ORIGINAL_PRICE = '//td[contains(text(),"List Price") or contains(text(),"M.R.P") or contains(text(),"Price")]/following-sibling::td/text()'
            XPATH_CATEGORY = '//a[@class="a-link-normal a-color-tertiary"]//text()'
            XPATH_AVAILABILITY = '//div[@id="availability"]//text()'

            RAW_NAME = doc.xpath(XPATH_NAME)
            RAW_SALE_PRICE = doc.xpath(XPATH_SALE_PRICE)
            RAW_CATEGORY = doc.xpath(XPATH_CATEGORY)
            RAW_ORIGINAL_PRICE = doc.xpath(XPATH_ORIGINAL_PRICE)
            RAw_AVAILABILITY = doc.xpath(XPATH_AVAILABILITY)

            NAME = ' '.join(''.join(RAW_NAME).split()) if RAW_NAME else None
            SALE_PRICE = ' '.join(''.join(RAW_SALE_PRICE).split()).strip() if RAW_SALE_PRICE else None
            CATEGORY = ' > '.join([i.strip() for i in RAW_CATEGORY]) if RAW_CATEGORY else None
            ORIGINAL_PRICE = ''.join(RAW_ORIGINAL_PRICE).strip() if RAW_ORIGINAL_PRICE else None
            AVAILABILITY = ''.join(RAw_AVAILABILITY).strip() if RAw_AVAILABILITY else None

            if not ORIGINAL_PRICE:
                ORIGINAL_PRICE = SALE_PRICE

            if page.status_code != 200:
                raise ValueError('captha')
            data = {
                'NAME': NAME,
                'SALE_PRICE': SALE_PRICE,
                'CATEGORY': CATEGORY,
                'ORIGINAL_PRICE': ORIGINAL_PRICE,
                'AVAILABILITY': AVAILABILITY,
                'URL': url,
            }
            print(data['NAME'])
            SongNames.append(data['NAME'])
            return data['NAME']
        except Exception as e:
            print(e)


def ReadAsin(AsinList):
    extracted_data = []
    for i in AsinList:
        url = "http://www.amazon.com/dp/" + i
        print("URL: " + url)
        extracted_data.append(AmzonParser(url))
        sleep(5)
    return extracted_data
    # f = open('data.json', 'w')
    #  json.dump(extracted_data, f, indent=4)


savedSongName = []


def savingSongName(songName):
    savedSongName.append(songName)
    f = open('savedPerferencingSong.json', 'w')
    json.dump(savedSongName, f, indent=4)


def ClearSongNames():
    global savedSongName
    savedSongName = []


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
    # tfidf(getAllTF("ccm"),getIdf(getAllTF("ccm")))
    # print('Cosine:', getCosin(getAdvancedQuery("interesting music"), reviewData[1]))
    # print(getSynonym("popular"))
    # print(getAdvancedQuery("interesting music"))
    # getMaxCosSim(getAdvancedQuery("interesting music"))
    # rankingResult(getMaxCosSim(getAdvancedQuery("dirty rap")))
    # rankingResult(getMaxCosSim(getAdvancedQuery(removeQueryStopwords("what is the most popular song by kanye west"))))
    # rankingResult(getMaxCosSim("what is the most popular song by kanye west"))
    # query = "happy glad funny"
    query = "money savage bad rap"
    print("Query: ", query)
    # print("Removed stop words query: ", removeQueryStopwords(query))
    # print("Advanced stop words query: ", getAdvancedQuery(removeQueryStopwords(query)))
    # print(getMaxTitleCosSim(getAdvancedQuery(removeQueryStopwords(query))))
    # print(getMaxArtistCosSim(getAdvancedQuery(removeQueryStopwords(query))))
    # for item in rankingResult(getMaxReviewCosSim(getAdvancedQuery(removeQueryStopwords(query))))[:5]:
    #     AsinList.append(item[0])
    # print(ReadAsin(AsinList))
    return



class Window(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        # create a prompt, an input box, an output label,
        # and a button to do the computation
        self.prompt = tk.Label(self, text="Search Query:", anchor="w")
        self.entry = tk.Entry(self)
        self.submit = tk.Button(self, text="Get Advanced Query", command=self.searchButton)
        self.output = tk.Label(self, text="Def Label")

        self.artistSubmit = tk.Button(self, text="Search Term Frequency", command=self.searchArtistButton)
        self.artistOutput = tk.Label(self, text="TF Label")

        # lay the widgets out on the screen.
        self.prompt.pack(side="top", fill="x")
        self.entry.pack(side="top", fill="x", padx=200)
        self.output.pack(side="top", fill="x", expand=True)
        self.submit.pack(side="top", fill='both', expand=True, padx=4, pady=4)

        self.artistOutput.pack(side="top", fill="x", padx=300, expand=True)
        self.artistSubmit.pack(side="top", fill='both', expand=True, padx=6, pady=6)

        self.SearchByTitle = tk.Button(self, text="Search By Title", command=self.searchByTitleButton)
        self.SearchByTitleOutput = tk.Label(self, text="Search By Title Label", wraplength=300, justify=LEFT)
        self.SearchByTitleOutput.pack(side="top", fill="x", padx=300, expand=True)
        self.SearchByTitle.pack(side="top", fill='both', expand=True, padx=8, pady=8)

        self.SearchByArtistName = tk.Button(self, text="Search By Artist Name", command=self.searchByArtistNameButton)
        self.SearchByArtistNameOutput = tk.Label(self, text="Search By Artist Name Label", wraplength=300, justify=LEFT)
        self.SearchByArtistNameOutput.pack(side="top", fill="x", padx=300, expand=True)
        self.SearchByArtistName.pack(side="top", fill='both', expand=True, padx=10, pady=10)

        self.SearchByReview = tk.Button(self, text="Search By Review", command=self.SearchByReviewButton)
        self.SearchByReviewOutput = tk.Label(self, text="Search By Review Label", wraplength=300, justify=LEFT)
        self.SearchByReviewOutput.pack(side="top", fill="x", padx=300, expand=True)
        self.SearchByReview.pack(side="top", fill='both', expand=True, padx=11, pady=11)

        var = StringVar(self)
        var.set("Song Name Index")  # initial value
        option = OptionMenu(self, var, "Song Name", "1", "2", "3", "4", "5", "None of them")
        option.pack()

        def ok():
            print("index is", var.get())
            try:
                savingSongName(SongNames[int(var.get()) - 1])
                print("saved songs: ", savedSongName)
            except ValueError:
                savingSongName("None_Result_Found")
                print("Selected None")

        button = Button(self, text="OK", command=ok)
        button.pack()

    # give top 5 results
    def SearchByReviewButton(self):
        query = str(self.entry.get())
        try:
            for item in rankingResult(getMaxReviewCosSim(getAdvancedQuery(removeQueryStopwords(query))))[:5]:
                AsinList.append(item[0])
            result = ReadAsin(AsinList)
        except ValueError:
            result = "invalid input"
        self.SearchByReviewOutput.configure(text=result)

    # give top 5 results
    def searchByArtistNameButton(self):
        query = str(self.entry.get())
        try:
            result = getMaxArtistCosSim(getAdvancedQuery(removeQueryStopwords(query)))[:5]
        except ValueError:
            result = "invalid input"

        self.SearchByTitleOutput.configure(text=result)

    # give top 5 results
    def searchByTitleButton(self):
        query = str(self.entry.get())
        try:
            result = getMaxTitleCosSim(getAdvancedQuery(removeQueryStopwords(query)))[:5]
        except ValueError:
            result = "invalid input"

        self.SearchByTitleOutput.configure(text=result)

    def searchArtistButton(self):
        # get the value from the input widget, convert
        # it to an int, and do a calculation
        try:
            i = str(self.entry.get())
            a = getAllTF(i)
            b = getIdf(getAllTF(i))
            c = tfidf(a, b)
            result = "Your query is: %s \n TF: %s , IDF: %s, TFIDF: %s" % (i, a, b, c)
        except ValueError:
            result = "Please enter string only"
        # set the output widget to have our result
        self.artistOutput.configure(text=result)

    def searchButton(self):
        # get the value from the input widget, convert
        # it to an int, and do a calculation
        try:
            i = str(self.entry.get())
            result = "Your query is: %s \n Filtered query is: %s \n Advanced query is: %s" % (
            i, removeQueryStopwords(i), getAdvancedQuery(removeQueryStopwords(i)))
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
    # ReadAsin()
