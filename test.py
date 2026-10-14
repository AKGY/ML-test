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
    response_loop = req.urlopen(url_article)
    soup_dic = BeautifulSoup(response_loop, "html.parser")
    content = soup_dic.select_one("#dic_area")
    #print("내용 : ",content.contents)
    output = ""

    for item in content.contents:
        stripped = str(item).strip()
        if stripped == "":
            continue
        if stripped[0] not in ["<","/"]:
            output += stripped

    print(output)
    print()

    time.sleep(1)