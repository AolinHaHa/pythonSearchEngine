# pythonSearchEngine
This is an intelligent music search engine including several features such as music/artist recommendation, saving search preference into json file; for the query modification we remove stop words then convert the original query with synonyms added; web crawler to keep tracking the song name by passing Amazon ASIN number; also calculate TFIDF value of any key words to see the importance of any specific term. The programming language that we used in this project is python.

## Implementation
We use local data as our data set, the data sets are 1M song database and Amazon music review dataset. Even we don’t have song name in the review dataset, but what we use is passing the ASIN number into a web crawler then grab the song name into local. Sometimes there are symbols in song title, to deal with that we change all symbols in dataset to a white space. ```text2Vector ()``` For the searching part, we convert query into vectors and using the converted vector to compare database and sort the cosine similarity. Therefore, in order to recommend the music to users, based on what other user reviewing the music we can find the most similar music review that matching the query. ```getMaxReviewCosSim ()``` Every time after user did a search we will save the result and write it into a json file. We use Tkinter to create the project GUI and also is an object-oriented project, we use inheritance to complete the functions amount the project. When we trying to grab the product info from amazon website, we’ve partially used ```AmazonParser ()``` as an outside source.

## Required Packages

_PyDictionary_

_pandas_

_scipy_

_itertools_

_operator_

_requests_

_warnings_


## Data Set
- **music.csv**


| Artist.name | Title    | Terms  |
| :---------  | --------:|  :--:  |
| Kanye West  | Stronger |  rap   |
| Andy Andy   | La Culpa |bachata |


- **reviews_Digital_Music_5.json**

| ReviewText  |    ASIN   |
| :---------  |    :--:   |
| "This is the third review of an irish..."  |5555991584 |
| "Many times, AND WITH GOOD REASON, the.."  |B0000000ZW |


## Key functions

`getCossinSim` - return cosine similarity for two strings (queries)

`text2Vector` - convert text to vectors and replace all non-letters with spaces

`getAllTF` - return term frequency of particular term

`getLST` - return everything in data frame into a list

`getSynonym` - return a list of synonym words

`removeQueryStopwords` - return a filtered query with all stopwords removed

`getAdvancedQuery` - return a stopwords-removed-query with all synonym words

`getArtistNameByIndex` -return artist name by passing record index

`getAllTF` - return term frequency by passing any particular term

`getIdf` - return IDF by passing any particular term

`tfidf` - return TFIDF by passing TF and IDF

`getSynonym` - return a list of synonym words

`getAdvancedQuery` - return a advanced query with stop words removed and synonyms added

`getAllArtist` - return all artist name

`getAllTitle` - return a list of titles

`getMaxReviewCosSim` - return cosine similarity between query and user reviews.

`getMaxTitleCosSim` - comparing query and titles, return a list of dicts with key=title name, value = cosin similarity

`getMaxArtistCosSim` - comparing query and artist names, return a list of dicts with key=title name, value = cosin similarity

`rankingResult` - groupby the getMaxReviewCosSim result by music ID, and get the average similarity score

`getAllTitle` - return a list of titles

`getMaxReviewCosSim` - return cosine similarity between query and user reviews.

`AmzonParser` - Amazon crawler, return product name and append into SongName based on amazon ASIN code and URL

`ReadAsin` - read a list of Amazon ASIN code and execute crawler

`savingSongName` - append into savedSongName and write into json file


## Future works
- [x] Analysis saved songs
- [ ] Generate analysis report, add weight into song name
- [ ] Running on server



## Questions Feedback?
- Email：<aolin.yang315@gmail.com>, <fangruivy@gmail.com>
