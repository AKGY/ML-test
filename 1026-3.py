from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import getpass

username = input("네이버 아이디: ")
password = getpass.getpass("네이버 비밀번호: ")

url = "https://nid.naver.com/nidlogin.login"
browser = webdriver.Chrome()

try:
    browser.implicitly_wait(10)
    browser.get(url)
    time.sleep(3)

    browser.save_screenshot("website_D.png")

    # 아이디 입력창을 찾아 기존 내용을 지우고 입력
    element_id = browser.find_element(By.ID, "id")
    element_id.clear()
    element_id.send_keys(username)

    # 비밀번호 입력창을 찾아 기존 내용을 지우고 입력
    element_pw = browser.find_element(By.ID, "pw")
    element_pw.clear()
    element_pw.send_keys(password)

    # 로그인 요청은 한 번만 실행
    element_pw.send_keys(Keys.ENTER)
    time.sleep(3)

    browser.save_screenshot("website_login.png")

    # 바로 종료하지 않고 화면 확인을 기다림
    print("브라우저에서 로그인 결과를 확인하세요.")
    print("보안문자나 추가 인증이 나오면 직접 진행하세요.")
    input("확인이 끝나면 이 터미널에서 Enter를 누르세요: ")

    browser.save_screenshot("website_Jp.png")
    print("최종 화면을 website_J.png에 저장했습니다.")

finally:
    browser.quit()
