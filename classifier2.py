import pandas as pd
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
import re
import string
import random

cols = ['sentiment','id','date','query_string','user','text']
loc = "C:/Users/risha/Downloads/NLP Data/"
df = pd.read_csv(loc+"emoticon.csv",header = None, names=cols,encoding = "ISO-8859-1")
df = df.drop(columns=['id','date','query_string','user'])
neg = random.randint(1,650000)
pos = random.randint(800000,1500000)

dataset = df.loc[neg:neg+100000,:] + df.loc[pos:pos+100000,:]
print(len(dataset))
print(dataset.head())
# k = 0
# for i in df.text:
#     print(type(i))
#     print(i)
#     k = k + 1
#     if k is 5:
#         break

# df = df.iloc[:10,]
print("Data Import Complete")

lem = WordNetLemmatizer()
sw_set = set(stopwords.words('english'))
dataset = []
for i in df.text:
    tweet = i.lower()
    tweet = re.sub(r"\A@\w+",'',tweet)
    tweet = re.sub(r"https\S+", '', tweet)
    tweet = re.sub(r"http\S+", '', tweet)
    tweet = tweet.strip(string.punctuation)
    token2 = re.sub('[^a-zA-Z]',' ', tweet).split()
    # print(token2)
    token3 = [lem.lemmatize(word) for word in token2 if word not in sw_set]
    # print(' '.join(token3))
    dataset.append(' '.join(token3))
    # if(len(dataset) >25):
    #     break

print("Cleaning Done")

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=1500)
X = cv.fit_transform(dataset).toarray()
y = df.iloc[:, 0].values
#
# print(cv.get_feature_names())
#
# # Splitting the dataset into the Training set and Test set
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)
#
# # Training the Naive Bayes model on the Training set
# import sklearn.naive_bayes as nb
# classifier = nb.GaussianNB()
# classifier.fit(X_train, y_train)
#
# # Predicting the Test set results
# y_pred = classifier.predict(X_test)