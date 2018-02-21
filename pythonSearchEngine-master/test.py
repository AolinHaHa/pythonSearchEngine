import imp
import sys
imp.reload(sys)
f = open("testdata.txt","r")
print (f)
word_list = []
filtered_words = []

def remove_stopwords():
	global filtered_words
	global word_list
	stopwords = [ "I", "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "could", "did", "do", "does", "doing", "down", "during", "each", "few", "for", "from", "further", "had", "has", "have", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "it", "it's", "its", "itself", "let's", "me", "more", "most", "my", "myself", "nor", "of", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "she", "she'd", "she'll", "she's", "should", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "we", "we'd", "we'll", "we're", "we've", "were", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "would", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves" ]
	for line in f.readlines():
		for word in line.split(' '):
			word_list.append(word)
	filtered_words = [item for item in word_list if item not in stopwords]


def searching (word, target):
	if word.lower() == target:
		return True
	

def getTF (term):
	global filtered_words
	count = 0
	found = 0
	for word in filtered_words:
		count += 1
		if searching (word, term) == True:
			found += 1 ##TF += 1
	print ("searching {} words".format(count))
	print ("found '{}' {} times".format(term, found))




remove_stopwords()
getTF("pleasure")
f.close()
