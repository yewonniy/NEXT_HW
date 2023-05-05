from bs4 import BeautifulSoup
import pandas as pd 
import requests as req

target_url ='https://opentutorials.org/course/1'

res = req.get(target_url)
soup = BeautifulSoup(res.text, 'html.parser')

li_comments = soup.find_all(class_= "comment_content")
li_comments_cleaned = [e.text.strip() for e in li_comments]
li_name = soup.select('div.name.time > strong')
li_name_cleaned = [e.text for e in li_name]
li_time = soup.select('div.name.time > a > time')
li_time_cleaned = [e.text for e in li_time]

container = {'comments':li_comments, 'name':li_name, 'time':li_time}
df_table = pd.DataFrame(container)
print(df_table)