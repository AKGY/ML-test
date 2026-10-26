import urllib.request as req
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"
response = req.urlopen(url)

soup = BeautifulSoup(response, "html.parser")
results = soup.select("a.sa_text_title")

for result in results:
    print("제목 : ", result.strong.string)
    print("링크 : ", result["href"] , "\n")