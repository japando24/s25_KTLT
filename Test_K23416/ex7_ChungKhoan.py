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
input_search.send_keys("ACB")

#%%
input_search.send_keys(Keys.ENTER)

#%%
#01/01/2025 - 12/02/2025
input_time=driver.find_element(By.XPATH,'//*[@id="date-inp-disclosure"]')
input_time.send_keys('01/01/2025 - 12/02/2025')
btn_Xem=driver.find_element(By.XPATH,'//*[@id="owner-find"]')
btn_Xem.click()

#%% DISPLAY DATA
def display_data():
    figure_table=driver.find_element(By.XPATH,'//*[@id="render-table-owner"]')
    tr_list=figure_table.find_elements(By.TAG_NAME,'tr')
    try:
        with open('data/stock_of_figure.json','r',encoding="utf8") as f:
            figures=json.load(f)
    except (FileNotFoundError,json.JSONDecodeError):
        figures=[]
    for tr in tr_list:
        for i in range (1,12):
            xpath_change=f'//*[@id="render-table-owner"]/tr[{i}]/td[4]'
            xpath_priceopen=f'//*[@id="render-table-owner"]/tr[{i}]/td[9]'
            figure={
                "Date": (tr.find_element(By.CLASS_NAME,'owner_time')).text,
                "PriceClose_thousandVND":(tr.find_element(By.CLASS_NAME,'owner_priceClose')).text,
                "Change": (tr.find_element(By.XPATH,xpath_change)).text,
                "PriceOpen_thousandVND":(tr.find_element(By.XPATH,xpath_priceopen)).text,
        }
        figures.append(figure)
    with open('data/stock_of_figure.json','w',encoding="utf8") as f:
        json.dump(figures,f,ensure_ascii=False,indent=4)

display_data()

#%% - CRAWL DATA
# time_out=25
# try:
#     WebDriverWait(driver, time_out).until(ec.visibility_of_element_located((By.CLASS_NAME,"oddOwner")))
# except TimeoutException:
#     print("Loading took too long")
#     driver.quit()
#Tìm số trang lớn nhất
max_pagenumber=driver.find_element(By.XPATH,'/html/body/div[8]/div/div[2]/div/div/div[7]/div/div[2]/div/a[5]')
max_page=int(max_pagenumber.text)
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
