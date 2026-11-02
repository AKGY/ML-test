from bs4 import BeautifulSoup
import urllib.request

url = "https://api.met.no/weatherapi/locationforecast/2.0/classic?lat=37.5665&lon=126.9780"

request = urllib.request.Request(
    url,
    headers={"User-Agent": "WeatherStudy/1.0 rsmfpos@gmail.com"}
)

xml = urllib.request.urlopen(request).read()

soup = BeautifulSoup(xml, "html.parser")

seoul = soup.find_all("location")[0]

print(seoul)