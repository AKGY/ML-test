import requests
import urllib.request as req
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time


USER = "zzzxwe@jj.ac.kr"
PASS = ""

session = requests.session()

login_info = {
    "email" : USER,
    "pass" : PASS
}

url_login = "https://www.facebook.com/?lsrc=cf"

res = session.post(url_login, data=login_info)
res.raise_for_status()

url_mypage = "https://www.facebook.com/profile.php?id=61594533277204"

res = session.get(url_mypage)
res.raise_for_status



print("상태 코드:", res.status_code)
print("최종 URL:", res.url)
