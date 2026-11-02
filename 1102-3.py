from bs4 import BeautifulSoup
import urllib.request

url = "https://xml-demo.weather.gov.hk/V3/bulletins/WeatherInformationForOtherCities_v3.xml"

response = urllib.request.urlopen(url)

xml = response.read()

soup = BeautifulSoup(xml, "xml")

seoul = soup.find_all("Location")[80]

print(seoul)
