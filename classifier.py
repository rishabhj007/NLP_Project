
# Creating the Bag of Words model
import preprocessing
import data_structuring

data = data_structuring.df
dt = preprocessing.getData(data_structuring.arr)
dataset = []

for list in dt:
    sentence = ""
    for words in list:
        sentence = sentence + " "+ words
    dataset.append(sentence)

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1000)
X = cv.fit_transform(dataset).toarray()
y = data.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

# Training the Naive Bayes model on the Training set
import sklearn.naive_bayes as nb
classifier = nb.GaussianNB()
classifier.fit(X_train, y_train)

# Predicting the Test set results
# y_pred = classifier.predict(X_test)
#
# # Making the Confusion Matrix
# from sklearn.metrics import confusion_matrix
# cm = confusion_matrix(y_test, y_pred)
# print(cm)


##twitter analysis

tweetData = preprocessing.getTweets()
TweetbagofWrds = cv.fit_transform(dataset).toarray()
y_pred_new = classifier.predict(TweetbagofWrds)
totalout = 0;
for i in range(len(tweetData)):
    print(tweetData[i])
    totalout = totalout + int(y_pred_new[i])
    
print(totalout)