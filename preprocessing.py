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
import string


def getTweets():
    lem = WordNetLemmatizer()
    sw_set = set(stopwords.words('english'))
    df = scrapping.main()
    dataset = []
    for i in df:
        tweet = i.lower()
        tweet = re.sub(r"\A@\w+", '', tweet)
        tweet = re.sub(r"https\S+", '', tweet)
        tweet = re.sub(r"http\S+", '', tweet)
        tweet = re.sub(r"pic\.twitter\.\S+", '', tweet)
        tweet = tweet.strip(string.punctuation)
        token2 = re.sub('[^a-zA-Z]', ' ', tweet).split()
        # print(token2)
        token3 = [lem.lemmatize(word) for word in token2 if word not in sw_set]
        # print(' '.join(token3))
        dataset.append(' '.join(token3))
        # if(len(dataset) >25):
        #     break
    print("Cleaning Done")
    return dataset

def getData(df):
    lem = WordNetLemmatizer()
    sw_set = set(stopwords.words('english'))
    dataset = []
    for i in df.text:
        tweet = i.lower()
        tweet = re.sub(r"\A@\w+", '', tweet)
        tweet = re.sub(r"https\S+", '', tweet)
        tweet = re.sub(r"http\S+", '', tweet)
        tweet = tweet.strip(string.punctuation)
        token2 = re.sub('[^a-zA-Z]', ' ', tweet).split()
        # print(token2)
        token3 = [lem.lemmatize(word) for word in token2 if word not in sw_set]
        # print(' '.join(token3))
        dataset.append(' '.join(token3))
        # if(len(dataset) >25):
        #     break
    print("Cleaning Done")
    return dataset
