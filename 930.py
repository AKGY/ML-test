import urllib.request as req
from bs4 import BeautifulSoup


url = "https://news.naver.com/section/105"

response = req.urlopen(url)

soup = BeautifulSoup(response, "html.parser")

results = soup.select("a.sa_text_title")

for result in results:
    
    print("제목: ", result.strong.string)

    url_article = result.attrs["href"]
    response = req.urlopen(url_article)

    soup = BeautifulSoup(response, "html.parser")
    print("링크: ", url_article)

    article = soup.select("#dic_area")
    print("내용: ", article.text)

    #soup_dic = BeautifulSoup(response, "html.parser")
    #content = soup_dic.select_one("dic_area")
    #print(content.contents)

    print("")   
    
