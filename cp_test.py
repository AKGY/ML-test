from seleniumbase import SB
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyperclip
pyperclip.set_clipboard("xclip")
import time
import getpass

url = "https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/"

USER = input("네이버 아이디: ")
PASS = getpass.getpass("네이버 비밀번호: ")

# SeleniumBase UC Mode 적용
with SB(
    uc=True,
    cft=True,
    xvfb=True,
    locale="ko",
    chromium_arg="--disable-dev-shm-usage"
) as sb:

    # WebDriver 연결을 일시적으로 해제한 상태에서 페이지 접속
    sb.uc_open_with_reconnect(url, reconnect_time=4)

    # 아이디 입력창이 나타날 때까지 대기
    sb.wait_for_element_visible("#id", timeout=15)

    # 기존 Selenium WebDriver 객체 사용
    browser = sb.driver

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
        sb.uc_click('[id="log.login"]')
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

        browser.find_element(By.ID, "log.login").click()
        time.sleep(2)

    mail_url = "https://mail.naver.com/"
    browser.get(mail_url)
    time.sleep(3)

    browser.save_screenshot("Website_3.png")

# with 블록 종료 시 브라우저 자동 종료