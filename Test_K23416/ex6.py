#%% Import lib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import json

#%% Config
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

#%% Crawl dataexam
url = "https://www.dienmayxanh.com/tu-lanh/tu-lanh-aqua-inverter-469-lit-aqr-m536xa-wgb?utm_flashsale=1"
driver = webdriver.Chrome()
driver.get(url)

#%% Display dataexam

#with open("test/testcmt.json", "w", encoding= "utf-8") as f:
#    json.dump(cmt_list, f, ensure_ascii=False, indent=3)

btn = driver.find_element(By.XPATH, '/html/body/section/div[2]/div[1]/div[10]/div[2]/div/div/div[6]/div/a')
btn.click()

#%% Run
cmt_list = driver.find_element(By.XPATH, '//*[@id="scrollList"]')
li_list = cmt_list.find_elements(By.TAG_NAME, "li")
cmt_list1 = []
for li in li_list:
        cmt = li.find_element(By.CLASS_NAME, 'cmt-txt').text
        user = li.find_element(By.CLASS_NAME, 'cmt-top-name').text
        cmt_list1.append({"user": user, "cmt": cmt})
print(cmt_list1)

#%%
with open("test/testcmt.json", "w", encoding= "utf-8") as f:
   json.dump(cmt_list1, f, ensure_ascii=False, indent=3)
#%% Change page

btn_next = driver.find_element(By.XPATH, "/html/body/div[8]/div/div[2]/div/div/div[7]/div[2]/div/a[4]")
btn_next.click()

#qua phải dừng lại một chúy