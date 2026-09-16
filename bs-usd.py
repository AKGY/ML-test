from bs4 import BeautifulSoup
import urllib.request as req

url = "https://stock.naver.com/market/marketindex"

res = req.urlopen(url)

soup = BeautifulSoup(res, "html.parser")