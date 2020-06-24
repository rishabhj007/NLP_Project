import pandas as pd
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

# Training the Naive Bayes model on the Training set
import sklearn.naive_bayes as nb
classifier = nb.MultinomialNB()
classifier.fit(X, y)
print("training complete")

#adding tweet functionality
tweetData = preprocessing.getTweets()
TweetBOW = cv.transform(tweetData)

# Predicting the Test set results
y_pred = classifier.predict(TweetBOW)

#print(y_pred) #commented the classification array
y_prob = classifier.predict_proba(TweetBOW)
totalout = 0;
for i in range(len(tweetData)):
    prob = y_prob.item((i,1)) 
    if(prob > .60):
        totalout = totalout + 1
    elif(.60>=prob>=.40):
        continue
    else:
        totalout = totalout +1


#print(totalout)
#redefined the output
print("Total POSITIVE tweets - Total NEGATIVE tweets = ",totalout)
if totalout > 5:
    print("Overall sentiment is POSITIVE")
elif totalout < 5:
    print("Overall sentiment is NEGATIVE")
else :
    print("Overall sentiment is Neutral")
=======
# print(totalout)

# totalout = 0;
# for i in range(len(tweetData)):
#     if(y_pred[i] == 0):
#         totalout -= 1
#     else:
#         totalout +=0

# print(totalout)

# Making the Confusion Matrix
# from sklearn.metrics import confusion_matrix
# cm = confusion_matrix(y_test, y_pred)
# print(cm)
