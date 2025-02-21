#%% IMPORT LIB
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import json
from time import sleep

from ext7_TM import time_out, xpath

#%% CRAWL DATA
url = "https://www.dienmayxanh.com/may-nuoc-nong/truc-tiep-ariston-4500w-aures-premium-45p-pearl"
driver = webdriver.Chrome()
driver.get(url)

time_out=25
try:
    WebDriverWait(driver, time_out).until(ec.visibility_of_element_located((By.CLASS_NAME,"cmt-txt")))
except TimeoutException:
    print("Loading took too long")
    driver.quit()

#%% REVIEW PAGE
#Click Xem đánh giá
btn_comments_page=driver.find_element(By.XPATH,'/html/body/section/div[2]/div[1]/div[8]/div[2]/div/div/div[6]/div/a')
btn_comments_page.click()
sleep(3)
#Tìm số trang lớn nhất
max_pagenumber=driver.find_element(By.XPATH,'/html/body/div[8]/div/div[2]/div/div/div[7]/div/div[2]/div/a[5]')
max_page=int(max_pagenumber.text)

#%% DISPLAY DATA
def display_data():
    #Lấy dataexam theo phân cấp
    comment_list =driver.find_element(By.ID,'scrollList')
    #Chọn TAG_NAME do mình cần ấy nhiều li, nếu dùng XPATH or ID chỉ có thể lấy only 1 thui
    li_list=comment_list.find_elements(By.TAG_NAME,'li')
    try:
        # Đọc file hiện có và add vô biến comments --> Lý do: tránh overwrite dữ liệu hiện có trong file
        with open('data/comments.json','r',encoding="utf8") as f:
            comments = json.load(f)
    except (FileNotFoundError,json.JSONDecodeError):
# Ở đây thêm các lỗi hay xảy ra nếu không tìm thấy file, lỗi file json
# Nếu không tồn tại gì thì tạo mới biến comments
        comments=[]
    for list in li_list:
        comment={
            "username": (list.find_element(By.CLASS_NAME,'cmt-top-name')).text,
            "comment": (list.find_element(By.CLASS_NAME,'cmt-txt')).text,
        }
        comments.append(comment)
    with open('data/comments.json','w',encoding="utf8") as f:
        json.dump(comments,f,ensure_ascii=False,indent=4)

#Save dataexam in first page
display_data()

#%% CRAWL DATA FROM OTHER PAGE
for i in range(2,max_page+1):
    xpath= f'//a[@href="javascript:ratingCmtList({i})" and text()="{i}"]'
    # Này là nút tương ứng với các số 2,3,4,...12 ứng với các giá trị i, bấm vô đây là qua trang tiếp theo
    # Phần xpath dài vậy do cái nút qua trang tiếp theo nó bị trùng href với title nên thêm 1 tiêu chí nữa là text(giá trị của tag đó) --> tránh trùng giá trị (lỗi)
    try:
        btn=driver.find_element(By.XPATH,xpath)
        btn.click()
        #Đợi 5 giây cho page load
        sleep(5)
        display_data()
    except:
        print("Error")
print("DONE!!!")