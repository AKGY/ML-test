import requests

url = "https://www.hanbit.co.kr/login?redirect=%2F"

session = requests.Session()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36"
}

res = session.get(url, headers=headers)

print("상태 코드:", res.status_code)
print("최종 URL:", res.url)
print(res.text[:500])


from bs4 import BeautifulSoup

soup = BeautifulSoup(res.text, "html.parser")

results = soup.select("input")

for result in results:
    print(result)


forms = soup.select("form")

for form in forms:
    print("action:", form.get("action"))
    print("method:", form.get("method"))