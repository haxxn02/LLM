#야놀자 리뷰 크롤링링
import time
from selenium import webdriver
from bs4 import BeautifulSoup

def crawl_yanolja_reviews(name, url):
    review_list = []
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2)
    
    
#js코드, 0부터 스크롤 끝까지 이동    
    scroll_count = 3
    for i in range(scroll_count):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')    
        time.sleep(2)
    #스크롤 내린 상태로 html 추출
    soup = BeautifulSoup(driver.page_source)
    #selector로 해당 컨테이너를 들고 올 수 있음음
    ##__next > section > div > div.css-1js0bc8 > div:nth-child(1) > div:nth-child(2) > div
    #selector에서 누구인지 찝어주는 nth-child(1) 같은 요소를 지워줘야 공통 요소를 가져옴
    review_containers = soup.select('#__next > section > div > div.css-1js0bc8 > div > div > div')
    
    for i in range(len(review_containers)):
        print(i)


#실행
crawl_yanolja_reviews('강릉 세인트존스호텔','https://nol.yanolja.com/reviews/domestic/3013417')
     
time.sleep(10)

