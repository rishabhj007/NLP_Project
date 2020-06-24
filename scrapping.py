import requests
from bs4 import BeautifulSoup


def getTweets(html):
    thislist = []
    for div in html.findAll("div", {"class": "dir-ltr"}):
        thislist.append(div.get_text())
    return thislist


def main():
    print("Please input the search HashTag")
    hashTag = str(input())  # HashTag input from user
    print("Please input the required Tweets")

    tweetNo = int(input())  # No of tweets required input from user
    tweetlist = []  # Empty list to contain tweets as strings

    hashTag.strip()  # removing any whitespaces
    if hashTag[0] == '#':  # removing hashTag char if present
        hashTag = hashTag[1:]
    hashTag.replace(" ", "")  # removing spaces

    url = "https://mobile.twitter.com/search?q=" + "%23" + hashTag  # twitter query url

    data = requests.get(url)  # getting the html of the search results
    html = BeautifulSoup(data.text, 'html.parser')  # changing raw data to html

    while True:
        if len(tweetlist) < tweetNo:
            tweetlist += getTweets(html)

            div = html.find("div", {"class": "w-button-more"}).find('a')
            url = "https://mobile.twitter.com" + div['href']

            data = requests.get(url)
            html = BeautifulSoup(data.text, 'html.parser')
        else:
            break
    return tweetlist


if __name__ == "__main__":
    main()
