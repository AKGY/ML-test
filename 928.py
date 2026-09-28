import urllib.request
from bs4 import BeautifulSoup

url = "https://m.stock.naver.com/marketindex/home/exchangeRate/exchange"

request = urllib.request.Request(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

with urllib.request.urlopen(request, timeout=10) as response:
    soup = BeautifulSoup(response, "html.parser")

# 미국·유럽·일본·중국 환율을 모두 선택
results = soup.select('a[href^="/marketindex/exchange/FX_"]')

for result in results:  
    row = result.find_parent("li")
    name = row.select_one("strong").get_text(strip=True)
    rate = row.select_one("b").get_text(strip=True)
    print(rate[0].sting)