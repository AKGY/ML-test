from selenium import webdriver

import time

url = "https://www.naver.com/"

# PhantomJS 드라이버 추출하기

browser = webdriver.PhantomJS()

# 3초간 대기하기

browser.implicitly_wait(10)

# URL 읽어들이기

browser.get(url)

browser.implicitly_wait(10)

time.sleep(3)

# 화면 캡쳐해서 저장하기

browser.save_screenshot("Website.png")

print("JS ERRORS:", browser.get_log("browser"))

browser.quit()