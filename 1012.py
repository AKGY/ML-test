#모듈 추출

import urllib.request as req
from bs4 import BeautifulSoup
import time

#기사 목록 호출하기

url = "http://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"

response = req.urlopen(url)

soup = BeautifulSoup(response,"html.parser")

results = soup.select("a.sa_text_title")

for result in results:
    #기사 가져오기
    print ("제목 : ", result.strong.string)
    url_article = result.attrs["href"]
    print("링크: ", url_article)

    response = req.urlopen(url_article)
    soup_dic = BeautifulSoup(response, "html.parser")
    content = soup_dic.select_one("#dic_area")

    #print(content.contents)
    #가공하기

    output = ""
    for item in content.contents:
        stripped = str(item).strip()
        if stripped == "":
            continue
        if stripped[0] not in ["<","/"]:
            output += str(item).strip()
    print(output)
    print()

    #1초간 휴식
    time.sleep(1)





