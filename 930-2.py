#모듈 추출


import urllib.request as req
from bs4 import BeautifulSoup

#기사 목록 가져오기
url = "https://news.naver.com/section/105"

response = req.urlopen(url)

soup = BeautifulSoup(response, "html.parser")

results = soup.select(".sa_text a")



for result in results:
    #기사 가져오기
    title = result.get_text()
    link = result.attrs["href"]

    if title :
        print("제목: ", title)
        print("링크: ", link)
        print("")

######

import time
#1초간 휴식
time.sleep(1)