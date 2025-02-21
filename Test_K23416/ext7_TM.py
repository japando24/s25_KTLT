#%% Import Lib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import json
from time import sleep
#%% - Crawl dataexam
url = "https://www.dienmayxanh.com/may-nuoc-nong/truc-tiep-ariston-4500w-aures-premium-45p-pearl"
driver = webdriver.Chrome()
driver.get(url)

time_out = 25
try:
    WebDriverWait(driver, time_out).until(ec.visibility_of_element_located((By.CLASS_NAME, "cmt-txt")))
except TimeoutException:
    print("Time out waiting for page to load!")
    driver.quit()

#%% Click vào trang đánh giá
btn_comments_page = driver.find_element(By.XPATH,"/html/body/section/div[2]/div[1]/div[8]/div[2]/div/div/div[6]/div/a")
btn_comments_page.click() #Nút "Xem 354 đánh giá"
sleep(3)
#Tìm ra số trang lớn nhất của page
number = driver.find_element(By.XPATH, "/html/body/div[8]/div/div[2]/div/div/div[7]/div[2]/div/a[4]")
#Nút có số 12
max_page = int(number.text)

#%% - Display dataexam
def display_data():
    comment_list = driver.find_element(By.ID,"scrollList")
    li_list = comment_list.find_elements(By.TAG_NAME, "li")
    try:
        # Đọc file hiện có và add vô biến comments --> Lý do: tránh overwrite dữ liệu hiện có trong file
        with open("data/comments.json", "r", encoding="utf-8") as f:
            comments = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError): #Ở đây thêm các lỗi hay xảy ra nếu không tìm thấy file, lỗi file json
        # Nếu không tồn tại gì thì tạo mới biến comments
        comments = []
    for list in li_list:
        comment = {
            "username": (list.find_element(By.CSS_SELECTOR, "p.cmt-top-name")).text,
            "comment": (list.find_element(By.CSS_SELECTOR, "p.cmt-txt")).text
        }
        comments.append(comment)
    with open("data/comments.json", "w", encoding="utf-8") as f:
        json.dump(comments, f, ensure_ascii=False, indent=4 )

#Save dataexam in first page
display_data()
#%% Lấy dữ liệu từ các trang

for i in range(2, max_page+1):
    xpath = f'//a[@href="javascript:ratingCmtList({i})" and text()="{i}"]'
    #Này là nút tương ứng với các số 2,3,4,...12 ứng với các giá trị i, bấm vô đây là qua trang tiếp theo
    #Phần xpath dài vậy do cái nút qua trang tiếp theo nó bị trùng href với title nên thêm 1 tiêu chí nữa là text(giá trị của tag đó) --> tránh trùng giá trị (lỗi)
    try:
        btn = driver.find_element(By.XPATH, xpath)
        btn.click()
        #Đợi 5 giây cho page load
        sleep(5)
        display_data()
    except:
        print("Lỗi")
print("Hoàn thành!!!")




