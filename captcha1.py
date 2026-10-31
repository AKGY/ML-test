
from seleniumbase import SB
import getpass
import time

url = "https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/"

USER = input("네이버 아이디: ")
PASS = getpass.getpass("네이버 비밀번호: ")

with SB(
    uc=True,
    cft=True,
    xvfb=True,
    locale="ko",
    chromium_arg="--disable-dev-shm-usage"
) as sb:

    # WebDriver 연결을 일시적으로 끊고 페이지 접속
    sb.uc_open_with_reconnect(url, reconnect_time=4)

    sb.wait_for_element_visible("#id", timeout=15)

    print("현재 URL:", sb.get_current_url())

    # 아이디 입력
    sb.type("#id", USER)
    time.sleep(2)

    # 비밀번호 입력
    sb.type("#pw", PASS)
    time.sleep(2)

    print("아이디 입력 확인:",
          sb.get_attribute("#id", "value") == USER)

    print("비밀번호 입력 확인:",
          sb.get_attribute("#pw", "value") == PASS)

    # 로그인 버튼 검색
    selectors = [
        '[id="log.login"]',
        'button[type="submit"]',
        '.btn_login'
    ]

    login_button = None

    for selector in selectors:
        if sb.is_element_visible(selector):
            login_button = selector
            break

    print("로그인 버튼:", login_button)

    # UC Mode 전용 클릭
    if login_button:
        sb.uc_click(login_button)
    else:
        sb.press_keys("#pw", "\n")

    time.sleep(5)

    print("로그인 후 URL:", sb.get_current_url())

    captcha = sb.is_element_visible("#captcha")
    print("CAPTCHA:", captcha)

    sb.save_screenshot("/sample/login_result.png")

    if captcha:
        print("CAPTCHA 발생")
    else:
        sb.uc_open_with_reconnect(
            "https://mail.naver.com/",
            reconnect_time=4
        )

        time.sleep(3)

        print("메일 URL:", sb.get_current_url())

        sb.save_screenshot("/sample/Website_Mail.png")

print("프로그램 종료")
