#%% Import Lib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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

#%% - CRAWL DATA

