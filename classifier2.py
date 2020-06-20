import pandas as pd
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
import re

cols = ['sentiment','id','date','query_string','user','text']
loc = "C:/Users/risha/Downloads/"
df = pd.read_csv(loc+"emoticon.csv",header = None, names=cols,encoding = "ISO-8859-1")
df = df.drop(columns=['id','date','query_string','user'])

# k = 0
# for i in df.text:
#     print(type(i))
#     print(i)
#     k = k + 1
#     if k is 5:
#         break

# df = df.iloc[:10,]
# print(df)

lem = WordNetLemmatizer()
sw_set = set(stopwords.words('english'))
dataset = []
for i in df.text:
    tweet = i.lower()
    token2 = re.sub('[^a-zA-Z]', ' ', tweet).split()
    token2 = [lem.lemmatize(word) for word in token2 if word not in sw_set]
    dataset.append(' '.join(token2))
#
# print(dataset)

from sklearn.feature_extraction.text import TfidfVectorizer
cv = TfidfVectorizer(max_features=1500,min_df= 52)
X = cv.fit_transform(dataset).toarray()
y = df.iloc[:, 0].values
#
# print(cv.get_feature_names())

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

# Training the Naive Bayes model on the Training set
import sklearn.naive_bayes as nb
classifier = nb.GaussianNB()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)