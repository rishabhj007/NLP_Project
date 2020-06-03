import requests
from bs4 import BeautifulSoup


def gettweets(html):
    thislist = []
    tweets = html.findAll("div", {"class": "dir-ltr"})
    for tweet in tweets:
        thislist.append(tweet)
    return thislist


print("Please input the search hashtag")
hashTag = str(input())  # HashTag input from user
print("Please input the required tweets")
tweetNo = int(input())  # No of tweets required input from user
tweetlist = []           # Empty list to contain tweets as strings
hashTag.strip()  # removing any whitespaces
if hashTag[0] == '#':  # removing hashTag char if present
    hashTag = hashTag[1:]
hashTag.replace(" ", "")  # removing spaces

url = "https://mobile.twitter.com/search?q=" + "%23" + hashTag  # twitter query url
print(url)
data = requests.get(url)  # getting the html of the search results
html = BeautifulSoup(data.text, 'html.parser')  # changing raw data to html
# print(html.get_text())
while True:
    if len(tweetlist) < tweetNo:
        tweetlist += gettweets(html)
        Div = html.find("div", {"class": "w-button-more"}).find('a')
        url = "https://mobile.twitter.com" + Div['href']
        print(url)
        data = requests.get(url)
        html = BeautifulSoup(data.text,'html.parser')
    else:
        break


def getlist():
    return tweetlist

