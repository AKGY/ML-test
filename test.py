import urllib.request as req
from bs4 import BeautifulSoup
import time


url = "http://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=104"

response = req.urlopen(url)

soup = BeautifulSoup(response, "html.parser")

results = soup.select("a.sa_text_title")

for result in results:
    print("제목 : ", result.strong.string)
    url_article = result.attrs["href"]
    print("링크 : ",url_article)
    #time.sleep(1)