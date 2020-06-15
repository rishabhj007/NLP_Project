# import string    #for punc
# import re   #for requests
# import pprint
#
# #opening html doc
# from urllib import request
# html = request.urlopen(url).read().decode('utf8')
#
# #cleaning html tags
# from bs4 import BeautifulSoup
# raw = BeautifulSoup(html, 'html.parser').get_text()
#
# #removing punctuations
# no_punc="".join([c for c in raw if c not in string.punctuation])
# raw2=no_punc

from nltk import word_tokenize
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
import re
import scrapping


def getTweets():
    lem = WordNetLemmatizer()
    sp = scrapping.main()
    sw_set = set(stopwords.words('english'))
    dataset = []
    for tweet in sp:
        # tokens = word_tokenize(tweet.lower())
        token2 = re.sub('[^a-zA-Z]', ' ', tweet).split()
        # tokens = [lem.lemmatize(word) for word in tokens if word not in SWset]
        token2 = [lem.lemmatize(word) for word in token2 if word not in sw_set]
        dataset.append(token2)
    return dataset

def getData(sp):
    lem = WordNetLemmatizer()
    sw_set = set(stopwords.words('english'))
    dataset = []
    for tweet in sp:
        # tokens = word_tokenize(tweet.lower())
        token2 = re.sub('[^a-zA-Z]', ' ', tweet).split()
        # tokens = [lem.lemmatize(word) for word in tokens if word not in SWset]
        token2 = [lem.lemmatize(word) for word in token2 if word not in sw_set]
        dataset.append(token2)
    return dataset
