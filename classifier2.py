import pandas as pd
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
import re
import string
import random
import preprocessing

cols = ['sentiment','id','date','query_string','user','text']
loc = "C:/Users/risha/Downloads/NLP Data/"
df = pd.read_csv(loc+"emoticon.csv",header = None, names=cols,encoding = "ISO-8859-1")
df = df.drop(columns=['id','date','query_string','user'])
neg = random.randint(1,650000)
pos = random.randint(800000,1500000)

neg = df.loc[neg:(neg+100000)]
pos = df.loc[pos:(pos+100000)]
df = pd.concat([neg,pos])

print("Data Import Complete")

dataset = preprocessing.getData(df)

from sklearn.feature_extraction.text import TfidfVectorizer
cv = TfidfVectorizer(max_features=1500)
X = cv.fit_transform(dataset).toarray()
y = df.iloc[:, 0].values

print("Vectorization finished")

# # Splitting the dataset into the Training set and Test set
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.10, random_state = 0)
#
# print("data split complete")

# Training the Naive Bayes model on the Training set
import sklearn.naive_bayes as nb
classifier = nb.MultinomialNB()
classifier.fit(X, y)

#adding tweet functionality
tweetData = preprocessing.getTweets()
TweetBOW = cv.transform(tweetData)

# Predicting the Test set results
y_pred = classifier.predict(TweetBOW)
print(y_pred)
totalout = 0;
for i in range(len(tweetData)):
    print(tweetData[i])
    if(int(y_pred[i]) == 0):
        totalout = totalout -1
    else:
        totalout = totalout +1

print(totalout)
# Making the Confusion Matrix
# from sklearn.metrics import confusion_matrix
# cm = confusion_matrix(y_test, y_pred)
# print(cm)