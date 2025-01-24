#%% -Import lib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

#%% - Config
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

#%% - Crawl Data
url ="https://vnexpress.net/sinh-vien-cua-toi-khong-ve-que-an-tet-de-o-lai-ha-noi-kiem-tien-4708513.html"
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

time_out=3
try:
    WebDriverWait(driver, time_out).until(ec.visibility_of_element_located((By.CLASS_NAME,"contentcomment")))
except TimeoutException:
    print("Timed out waiting for page to load")
    driver.quit()


#%% - Display data
comments = driver.find_elements(By.CLASS_NAME, "contentcomment")
for comment in comments:
    print(comment.text)