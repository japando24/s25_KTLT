#%% Import Lib
import json
from cgitb import text
from time import sleep

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

#%%
driver = webdriver.Chrome()
url="https://cafef.vn/du-lieu.chn"
driver.get(url)


#%%
btn_lichsu=driver.find_element(By.XPATH,'//*[@id="pagewrap"]/div[1]/div[1]/div[2]/a[3]')
btn_lichsu.click()

#%%
input_search=driver.find_element(By.ID,'ContentPlaceHolder1_ctl00_acp_inp_disclosure')
input_search.send_keys("TCB")
input_search.send_keys(Keys.ENTER)


#%%
#01/01/2023 - 31/12/2023
input_time=driver.find_element(By.XPATH,'//*[@id="date-inp-disclosure"]')
input_time.send_keys('01/01/2023 - 31/12/2023')
btn_Xem=driver.find_element(By.XPATH,'//*[@id="owner-find"]')
btn_Xem.click()

#%% DISPLAY DATA
def display_data():
    figure_table=driver.find_element(By.XPATH,'//*[@id="render-table-owner"]')
    tr_list=figure_table.find_elements(By.TAG_NAME,'tr')
    try:
        with open('exam14022025/dataexam/data_e4.json','r',encoding="utf8") as f:
            figures=json.load(f)
    except (FileNotFoundError,json.JSONDecodeError):
        figures=[]
    for tr in tr_list:
        for i in range (1,12):
            xpath_high=f'//*[@id="render-table-owner"]/tr[{i}]/td[10]'
            xpath_low=f'//*[@id="render-table-owner"]/tr[{i}]/td[11]'
            xpath_priceopen=f'//*[@id="render-table-owner"]/tr[{i}]/td[9]'
            figure={
                "Date": (tr.find_element(By.CLASS_NAME,'owner_time')).text,
                "High":(tr.find_element(By.XPATH,xpath_high)).text,
                "Low": (tr.find_element(By.XPATH,xpath_low)).text,
                "Open":(tr.find_element(By.XPATH,xpath_priceopen)).text,
                "Close": (tr.find_element(By.CLASS_NAME, 'owner_priceClose')).text,
        }
        figures.append(figure)
    with open('exam14022025/dataexam/data_e4.json','w',encoding="utf8") as f:
        json.dump(figures,f,ensure_ascii=False,indent=4)

display_data()

#%% - CRAWL DATA
#Tìm số trang lớn nhất
max_page=13
for i in range (1,max_page+1):
    xpath=f'//*[@id="wraper-content-paging"]/div[{i}]'
    try:
        btn = driver.find_element(By.XPATH, xpath)
        btn.click()
        # Đợi 5 giây cho page load
        sleep(5)
        display_data()
    except:
        print("Error")
print("DONE!!!")
