#네이버 웹툰 댓글 크롤링
#https://comic.naver.com/webtoon/detail?titleId=823195&no=125&week=wed
import time
from selenium import webdriver
from bs4 import BeautifulSoup

#크롬창 지정
driver = webdriver.Chrome()
#페이지 이동
driver.get("https://comic.naver.com/webtoon/detail?titleId=823195&no=125&week=wed")

#selenium이 가져온 html을 bs에 넣음
soup = BeautifulSoup(driver.page_source)
comment_area = soup.find_all('span',{'class', 'u_cbox_contents'})
print('* * * * * * * * * * 베스트 댓글 * * * * * * * * * *')
for i in range(len(comment_area)):
    comment = comment_area[i].text.strip()
    print(comment)
    print('-' * 30)


#celenium은 글자 작성, 엔터키, 클릭 모두 할 수 있기 때문에 편리함
#full xpath 이용
#/html/body/div[1]/div[5]/div/div/div[4]/div[1]/div[3]/div/div/div[4]/div[1]/div/ul/li[2]/a/span[2]
driver.find_element('xpath', '/html/body/div[1]/div[5]/div/div/div[4]/div[1]/div[3]/div/div/div[4]/div[1]/div/ul/li[2]/a/span[2]').click()

time.sleep(2)

#전체댓글 클릭한 페이지 코드 불러오기
soup = BeautifulSoup(driver.page_source)
comment_area = soup.find_all('span',{'class', 'u_cbox_contents'})
print('* * * * * * * * * * 전체 댓글 * * * * * * * * * *')
for i in range(len(comment_area)):
    comment = comment_area[i].text.strip()
    print(comment)
    print('-' * 30)



time.sleep(30)
