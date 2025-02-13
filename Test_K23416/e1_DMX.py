#%% - Import library
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import json

from ex5 import chrome_options

#%% - Config
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

#%% - Crawl Data
url = "https://www.dienmayxanh.com/may-giat/samsung-ai-ww10t634dlx-sv"
driver = webdriver.Chrome(options=chrome_option)
driver.get(url)

time_out = 60
try:
    WebDriverWait(driver, time_out).until(ec.visibility_of_element_located(By.CLASS_NAME,"cmt-txt"))
except TimeoutException:
    print("Timed out waiting for page to load")
    driver.quit()

#%% - Display data
comment_list = driver.find_element(By.XPATH,"/html/body/section/div[2]/div[1]/div[8]/div[2]/div/div/div[6]/ul")
li_list=comment_list.find_elements(By.TAG_NAME,"li")
#print(li_list[0].find_elements(By.CLASS_NAME,"cmt-top-name").text)
#print(li_list[0].find_element(By.CSS_SELECTOR,"p.cmt-top-name").text)
#print(li_list[0].find_element(By.CSS_SELECTOR,"p[class='cmt-top-name']").text)
#print(li_list[0].find_element(By.CSS_SELECTOR,"cmt-top-name").text)

cmt_list=[]
for li in li_list:
    cmt = li.find_element(By.CLASS_NAME, 'cmt-txt').text
    user = li.find_element(By.CLASS_NAME, 'cmt-top-name').text
    cmt_list.append({
        "user":user,
        "comment":cmt
    })
print(cmt_list)

#old code
# cmt_list = []
# for comment in comments:
#     #print(comment.text)
#     cmt_list.append({"comment":comment.text})
# print(cmt_list)


#%% - Save json
with open ("data/e1_ĐMX.json","w",encoding="utf8") as f:
    json.dump(cmt_list,f,indent=3,ensure_ascii=False)
    #ensure_ascii: lưu TV ; indent=3: 3 khoảng trống ứng với 1 tab

#%% - Button View All Review
btn = driver.find_element(By.XPATH,"/html/body/section/div[2]/div[1]/div[9]/div[2]/div/div/div[6]/div/a")
btn.click()

#%%
btn_next=driver.find_element(By.XPATH,'/html/body/div[8]/div/div[2]/div/div/div[7]/div/div/div/a[5]')
btn_next.click()

#%%
from time import sleep
for i in range(5):
    sleep(3)

#Bài ktra sẽ phức tạp sẽ tuương tự khác data