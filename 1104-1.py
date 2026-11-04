from bs4 import BeautifulSoup
import urllib.request

url = "https://web.archive.org/web/20240303030113id_/https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"

response = urllib.request.urlopen(url)

xml = response.read()

soup = BeautifulSoup(xml, "html.parser")

seoul = soup.find_all("location")[0]

datas = seoul.find_all("data")

for item in datas:
    print(item.find("wf").text)







warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
