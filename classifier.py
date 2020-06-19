
# Creating the Bag of Words model
import preprocessing
import data_structuring
# from nltk.corpus import twitter_samples
#
# pos = twitter_samples.strings('positive_tweets.json')
# neg = twitter_samples.strings('negative_tweets.json')
# posData = preprocessing.getData(pos)
# negData = preprocessing.getData(neg)
#
# df1 = pd.DataFrame(negData,columns = ['Text'])
# df1 = df1.assign(Sent=0)
#
# df2 = pd.DataFrame(posData,columns = ['Text'])
# df2.assign(Sent=1)
#
# df = pd.concat([df1, df2, df3])

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
classifier = nb.BernoulliNB()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)