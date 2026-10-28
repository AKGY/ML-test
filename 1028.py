from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import getpass

url = "https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/"

USER = input("네이버 아이디: ")
#PASS = getpass.getpass("네이버 비밀번호: ") #비밀번호 보안입력
PASS = input("네이버 비밀번호: ")

#드라이버 추출하기

#options = webdriver.FirefoxOptions()
#options.add_argument("-headless")
#browser = webdriver.Firefox()

options = webdriver.FirefoxOptions()

browser = webdriver.Remote(
    command_executor="http://selenium-firefox:4444",
    options=options
)

# 3초간 대기하기
browser.implicitly_wait(3)

# URL 읽어들이기
browser.get(url)

#내 코드 집어넣기


element_id = browser.find_element(By.ID,"id") #id텍스트 입력상자
element_id.clear()
element_id.send_keys(USER)
element_pw = browser.find_element(By.ID,"pw") #비번 텍스트 입력상자
element_pw.clear()
element_pw.send_keys(PASS)
time.sleep(1)

element_pw.send_keys(Keys.ENTER)
time.sleep(1)
input("CAPTCHA 해결 후 Enter를 누르세요: ")
# 화면 캡쳐해서 저장하기

url_mail = "https://mail.naver.com/"
browser.get(url_mail)
browser.save_screenshot("Website_H.png")



titles = browser.find_elements(By.CSS_SELECTOR, "li.mail_item span.text")

for title in titles:
    print("-", title.text)

#종료
browser.quit()
