from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
pyperclip.set_clipboard("xclip")
import time
import getpass

url = "https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/"

service = Service('/usr/local/bin/geckodriver')

options = webdriver.FirefoxOptions()
options.add_argument("-headless")

browser = webdriver.Firefox(service=service, options=options)

browser.get(url)

USER = input("네이버 아이디: ")
PASS = getpass.getpass("네이버 비밀번호: ") #비밀번호 보안입력
#PASS = input("네이버 비밀번호: ")

pyperclip.copy(USER)
element_id = browser.find_element(By.ID, "id")
element_id.send_keys(pyperclip.paste())
time.sleep(2)

pyperclip.copy(PASS)
element_pw = browser.find_element(By.ID, "pw")
element_pw.send_keys(pyperclip.paste())
time.sleep(2)

login_buttons = browser.find_elements(By.ID, "log.login")

if login_buttons:
    login_buttons[0].click()
else:
    element_pw.send_keys(Keys.ENTER)
time.sleep(2)

capcha_elements = browser.find_elements(By.ID, "captcha")

if capcha_elements:
    print("캡챠가 있습니다.")

    browser.save_screenshot("Website_Captcha.png")

    element_captcha = browser.find_element(By.ID, "captcha")
    captcha_input = input("캡챠를 입력하세요: ")

    element_captcha.send_keys(captcha_input)
    time.sleep(2)

    login_button = browser.find_element(By.ID, "log.login").click()
    time.sleep(2)

mail_url = "https://mail.naver.com/"
browser.get(mail_url)
time.sleep(3)
    
browser.save_screenshot("Website_3.png")

browser.quit()