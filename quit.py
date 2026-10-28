from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


url = "https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/"



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


#종료
browser.quit()