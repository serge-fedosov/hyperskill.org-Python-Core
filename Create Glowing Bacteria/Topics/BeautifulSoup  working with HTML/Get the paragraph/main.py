import requests

from bs4 import BeautifulSoup

word = input()
url = input()
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
paragraphs = soup.find_all('p')
for p in paragraphs:
    string = p.text
    if word in string:
        print(string)
