import requests

from bs4 import BeautifulSoup

letter = 'S'
url = input()
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
a = soup.find_all('a')

start = False
stop = False
result = []
for i in a:
    t = i.text

    if t == "Schistosomiasis":
        start = True

    if start and not stop and len(t) > 1 and t.startswith(letter):
        result.append(i.text)

    if t == "Sustainable Development Goals":
        stop = True

print(result)
