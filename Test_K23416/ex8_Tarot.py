#%%
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#%%
url='https://tarot.vn/dien-giai-xuoi-cua-la-bai-the-fool-trong-tarot/'
driver=webdriver.Chrome()
driver.get(url)

#%%
div_element=driver.find_element(By.XPATH,'//*')
p_elements=driver.find_element(By.XPATH,'//*')