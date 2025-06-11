# 구글 검색

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://www.google.com')
#name이 q인 속성을 찾음
search = driver.find_element('name', 'q') 
search.send_keys('날씨')
search.send_keys(Keys.RETURN) #=> Enter키까지 입력

time.sleep(10)