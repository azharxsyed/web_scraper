# Building a Web Scraper

import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/White_Nights_(1957_film)"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
}
response = requests.get(URL, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

print(response.status_code)

#print(response.text)

title = soup.title.get_text()

print(title)

heading = soup.h1.get_text()
print(heading)
