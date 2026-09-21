import urllib.request
from bs4 import BeautifulSoup
import time

url = "https://news.naver.com/section/101"
response = urllib.request.urlopen(url)

soup = BeautifulSoup(response, "html.parser")
results = soup.select("#newsct")

for result in results:
    result_tag = result.select("div.sa_text > a")
    print(result_tag)

    a = 1

    for title_tag in result_tag:
        strong = title_tag.select_one("strong")
        link = title_tag.attrs["href"]

        if strong:
            title = strong.get_text().strip()
        else:
            title = None

        print("제목:", title)
        print("링크:", link)
        print("")

        url_article = title_tag.attrs["href"]
        response = urllib.request.urlopen(url_article)
        soup_dic = BeautifulSoup(response, "html.parser")
        content = soup_dic.select_one("#dic_area")

        if content:
            output = ""

            for item in content:
                stripped = str(item).strip()

                if stripped == "":
                    continue

                if stripped[0] not in ["<", "/"]:
                    output += stripped + " "

            print("본문 :", output.strip())

        else:
            print("본문 내용을 찾을 수 없습니다.")

        print("")
        time.sleep(1)