import urllib.request

from bs4
import BeautifulSoup

url = "https://news.naver.com/section/105"

response = urllib.request.urlopen()

soup = BeautifulSoup(response, "html.parser")
soup.select_one()
results = soup.select()

for sesult in results:
    print(results.string)