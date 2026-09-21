import urllib.request

from bs4
import BeautifulSoup

url = ""

response = urllib.request.urlopen()

soup = BeautifulSoup(response, "html.parser")
soup.select_one()
results = soup.select()

for sesult in results:
    print(results.string)