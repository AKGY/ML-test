from bs4 import BeautifulSoup
import urllib.request

url = "https://weather-broker-cdn.api.bbci.co.uk/en/forecast/rss/3day/1835848"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
req = urllib.request.Request(url, headers=headers)
request = urllib.request.urlopen(req)

xml = request.read()

soup = BeautifulSoup(xml, "xml")
seoul = soup.find_all("title")[0]
weather = soup.find_all("item")[0]

print("장소: " ,seoul)
print("날씨: " ,weather)