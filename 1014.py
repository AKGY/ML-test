import requests
import urllib.request as req
from urllib.parse import urljoin


#session.delete(url)
#session.post(url)
#session.put(url)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36"
}

url = "https://www.hanbit.co.kr/api/auth/callback/general-credentials"


session = requests.session()

url_csrf = "https://www.hanbit.co.kr/api/auth/csrf"

res = session.get(url_csrf)
res.raise_for_status()

csrf_token = res.json()["csrfToken"]



session.headers.update(headers)

USER = ""
PASS = ""
data = { 
    "loginId": USER,
    "password": PASS,
    "redirect": "false",
    "csrfToken": csrf_token,
    "callbackUrl": "https://www.hanbit.co.kr/my/shopping?tab=mileage",
    "json": "true"

}


res = session.post(url, data=data) 

url_my = "https://www.hanbit.co.kr/my"

res = session.get(url_my)
res.raise_for_status

print(res.text)
print("상태 코드:", res.status_code)
print("최종 URL:", res.url)