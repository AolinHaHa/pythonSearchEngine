# pythonSearchEngine
Python intelligent data retrieval Search Engine 


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



## Questions feedbacks?
- Email：<aolin.yang315@gmail.com>, 
