from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service #추가한거,,
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver = "C:/Users/ae665/Desktop/NEXT_HW/session5/chromedriver.exe"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) #바꾼거,,

# 실행할 웹페이지 불러오기 (네이버영화)
driver.get("https://movie.naver.com/")

#랭킹 1~20위
rankbtn = driver.find_element(By.XPATH, '//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a')
rankbtn.click()
time.sleep(3)

for i in range(2,22) :
    try:
        one_to_twenty = driver.find_element(By.XPATH, f'/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[{i}]/td[2]/div/a').text
        print(one_to_twenty)
    except:
        print("?")

#각 영화 클릭 -> 개요, 감독, 평점
suzeme = driver.find_element(By.XPATH, '/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[3]/td[2]/div/a')
suzeme.click()
time.sleep(2)
try:
    genre = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[1]/a').text
    director = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a').text
    print(genre, director)
except:
    print("? ?")

try:
    rating = driver.find_element(By.XPATH, "/html/body/div/div[4]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/a/div/span/span").text
    nums = rating.split()[2][:4]
    print(rating,nums)
except:
    print("없네?")

# for i in range(1,5) :
#     try:
#         rating = driver.find_element(By.XPATH, f'/html/body/div/div[4]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/a/div/em[{i}]').text
#         print(rating)
#     except:
#         print("별점 없음")

#내가 좋아하는 영화 검색 -> 제목, 감독, 스크롤 내려서 평점, 리뷰 개수
search = driver.find_element(By.XPATH, '//*[@id="ipt_tx_srch"]')
search.send_keys("더 퍼스트 슬램덩크")
search.send_keys(Keys.ENTER)
time.sleep(2)
moviebtn = driver.find_element(By.XPATH, '//*[@id="old_content"]/ul[2]/li/dl/dt/a')
moviebtn.click()
time.sleep(2)

#csv 파일로 저장
file = open('movie.csv', mode = 'w', newline='')
writer = csv.writer(file)
writer.writerow(["title","director","rating", "review"])

#↓ 제목, 감독
title = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/h3/a[1]').text
director = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a').text
#↓ 스크롤 두 번 내리기
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN) 
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
#↓ 평점, 리뷰수
rating = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[4]/div[5]/div[2]/div[2]/div[1]/div/div/em').text
review = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[4]/div[5]/div[2]/div[3]/strong/em').text

print(title, director, rating, review)

writer.writerow([title, director, rating, review])
file.close()