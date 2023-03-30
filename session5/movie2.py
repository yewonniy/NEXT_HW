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

file = open('movie2.csv', mode = 'w', newline='')
writer = csv.writer(file)
writer.writerow(["title","director","rating", "review"])

for i in range(2,22):
    try:
        movie = driver.find_element(By.XPATH, f'/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[{i}]/td[2]/div/a')
        movie.click()
        #각 영화 들어가기
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
    except:
        print("뭔가 에러가 있네")
     #뒤로가기 혹은 영화랭킹 누르는 코드
    back = driver.find_element(By.XPATH, f'//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a')
    back.click()
    time.sleep(3)


file.close()