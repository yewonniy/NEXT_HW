from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
from selenium.webdriver.common.action_chains import ActionChains


# 디버깅 모드
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver = "C:/Users/ae665/Desktop/Session5/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, options= chrome_options)

# 실행할 웹페이지 불러오기 (멜론 차트)
driver.get("https://www.melon.com/index.htm")

# 멜론 차트 버튼 클릭
chartbutton = driver.find_element(By.XPATH, '//*[@id="gnb_menu"]/ul[1]/li[1]/a/span[2]')
chartbutton.click()

# 1위곡명 가져오기
first = driver.find_element(By.XPATH, '//*[@id="lst50"]/td[6]/div/div/div[1]/span/a').text
print(first)
time.sleep(3)

# 1위부터 20위까지 가져오기
#for i in range(1,21):
#    twenty = driver.find_element(By.XPATH, f"/html/body/div/div[3]/div/div/div[3]/form/div/table/tbody/tr[{i}]/td[6]/div/div/div[1]/span/a").text
#    print(twenty)

# 스크롤 내리기

# 실시간 급상승 가수 가져오기 (마우스 위치를 조정해주어야 함 -> ActionChains 함수)
#elem = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div[2]/div')
#mouse = ActionChains(driver).move_to_element(elem)
#mouse.perform()

#for i in range(1,11):
#    singer = driver.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div/div[1]/div[2]/div/ol/li[{i}]/a').text
#    print(singer)

# 곡의 장르 가져오기
#genrebtn = driver.find_element(By.XPATH, '//*[@id="lst50"]/td[4]/div/a')
#genrebtn.click()

#genre = driver.find_element(By.XPATH, '//*[@id="conts"]/div[2]/div/div[2]/div[2]/dl/dd[2]').text
#print(genre)

# 좋아하는 가수의 곡명 10개 (검색창 키고 sendkeys) .send_keys(key,enter) 하면 엔터치는 효과
#search = driver.find_element(By.XPATH, '//*[@id="top_search"]')
#ActionChains(driver).send_keys_to_element(search, "엔시티드림").perform()
#button = driver.find_element(By.XPATH, '//*[@id="gnb"]/fieldset/button[2]')
#button.click()

#time.sleep(2)
#for i in range(1,11):
#    song = driver.find_element(By.XPATH, f"/html/body/div/div[3]/div/div[1]/div[4]/div/form[1]/div/table/tbody/tr[{i}]/td[3]/div/div/a[2]").text
#    print(song)

# 순위, 곡명, 가수명 가져오기
#file = open('melon.csv', mode = 'w', newline='')
#writer = csv.writer(file)
#writer.writerow(["rank","songs","singers"])

#time.sleep(3)
#for i in range(1,101) :
#    rank = driver.find_element(By.XPATH, f"/html/body/div/div[3]/div/div/div[3]/form/div/table/tbody/tr[{i}]/td[2]/div/span[1]").text
#    singers = driver.find_element(By.XPATH, f'/html/body/div/div[3]/div/div/div[3]/form/div/table/tbody/tr[{i}]/td[6]/div/div/div[2]/a').text
#    songs = driver.find_element(By.XPATH, f"/html/body/div/div[3]/div/div/div[3]/form/div/table/tbody/tr[{i}]/td[6]/div/div/div[1]/span/a").text
#    print(rank, singers, songs)

# csv 파일로 변환
#    writer.writerow([rank, songs, singers])
#file.close()