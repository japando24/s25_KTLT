#%% IMPORT LIB
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import json
from time import sleep

#%% CRAW DATA
url = 'https://cellphones.com.vn/laptop/mac.html'
driver = webdriver.Chrome()
driver.get(url)

time_out=25
try:
    WebDriverWait(driver, time_out).until(ec.visibility_of_element_located((By.CLASS_NAME,"product-info")))
except TimeoutException:
    print("Loading took too long")
    driver.quit()

#%% SHOW MORE
btn_showmore=driver.find_element(By.CLASS_NAME,"button btn-show-more button__show-more-product")
for i in range (1,6):
    btn_showmore.click()
    i +=1
#%% DISPLAY DATA
def display_data():
    product_list=driver.find_elements(By.CLASS_NAME,"product-list-filter is-flex is-flex-wrap-wrap")
    item_list=product_list.find_elements(By.CLASS_NAME,"product-info-container product-item")
    try:
        with open('exam14022025/dataexam/data_e2.json', 'r', encoding="utf8") as f:
            products = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        products=[]
    for item in item_list:
        product={
            "product_name": (item.find_element(By.CLASS_NAME,"product__name")),
            "img": (item.find_element(By.TAG_NAME,"img")),
            "product_price": (item.find_element(By.CLASS_NAME,"product__price--show")),
            "promotion": (item.find_element(By.CLASS_NAME,"coupon-price")),
        }
    with open('exam14022025/dataexam/data_e2.json','w',encoding="utf8") as f:
        json.dump(products,f,ensure_ascii=False,indent=4)
display_data()





