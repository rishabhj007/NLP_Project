import requests
from bs4 import BeautifulSoup

hashTag = input()             # HashTag input from user
hashTag.strip()               # removing any whitespaces
if hashTag[0] == '#':         # removing hashTag char if present
    hashTag = hashTag[1:]
hashTag.replace(" ", "")      # removing spaces

url = "https://mobile.twitter.com/search?q=" + "%23" + hashTag         # twitter query url
print(url)
data = requests.get(url)                                        # getting the html of the search results
html = BeautifulSoup(data.text, 'html.parser')                  # changing raw data to html
print(html.get_text())

