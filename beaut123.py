import requests

url = "http://google.com"

session = requests.Session()
response = session.get(url)

response.raise_for_status()

print(response.text)