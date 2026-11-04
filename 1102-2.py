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

browser = webdriver.Firefox(service=service)

browser.get(url)

id = input("네이버 아이디: ")
pw = getpass.getpass("네이버 비밀번호: ")

pyperclip.copy(id)
element_id.clear()
element_id = browser.find_element(By.ID, "id")
element_id.send_keys(pyperclip.paste())
time.sleep(2)

pyperclip.copy(pw)
element_pw.clear
element_pw = browser.find_element(By.ID, "pw")
element_pw.send_keys(pyperclip.paste())
time.sleep(2)

login_buttons = browser.find_elements(By.ID, "log.login")

if login_buttons:
    login_buttons[0].click()
else:
    element_pw.send_keys(Keys.ENTER)

time.sleep(2)

captcha_elements = browser.find_elements(By.ID, "captcha")


if captcha_elements:
    print("캡챠가 있습니다.")
    browser.save_screenshot("/sample/Website_Captcha_1102.png")

    cp = input("캡챠를 입력하세요: ")

    pyperclip.copy(cp)

    element_captcha = browser.find_element(By.ID, "captcha")
    element_captcha.send_keys(pyperclip.paste())

    # CAPTCHA 입력 후 로그인 제출
    element_captcha.send_keys(Keys.ENTER)

    time.sleep(2)




mail_url = "https://mail.naver.com/"

#다시한번
pyperclip.copy(id)
element_id.clear()
element_id = browser.find_element(By.ID, "id")
element_id.send_keys(pyperclip.paste())
time.sleep(2)

pyperclip.copy(pw)
element_pw.clear()
element_pw = browser.find_element(By.ID, "pw")
element_pw.send_keys(pyperclip.paste())
time.sleep(2)

login_buttons = browser.find_elements(By.ID, "log.login")

if login_buttons:
    login_buttons[0].click()
else:
    element_pw.send_keys(Keys.ENTER)

time.sleep(2)

browser.get(mail_url)
time.sleep(3)

browser.save_screenshot("Website_3.png")
browser.quit()