#%% - Import lib
import requests as rq
from bs4 import BeautifulSoup as bs

#%% - Crawl dataexam from url
url ="https://tuoitre.vn/tin-tuc-sang-24-1-cach-ne-ket-xe-khi-ve-mien-tay-an-tet-khai-mac-hoi-hoa-xuan-tp-hcm-20250123050435873.htm"
response = rq.get(url)

#%% - Display dataexam
if response.status_code == 200:
    returned_data = response.text
    # print(returned_data)
    soup = bs(returned_data, "html.parser")
    # title = soup.find("title")
    # print(title.text)

    # sub_title = soup.find("h2",class_="detail-sapo").text #Cách 1
    # sub_title=soup.find("h2",{"class": "detail-sapo"}).text #Cách 2
    # print(sub_title)

    comment = soup.find("span",{"class":"contentcomment"}).text
    print(comment)

#%% - Note
"""
Client gửi yêu cầu lên Server

Server-Side Rendering  --- Client-Side Rendering
Client-Side: html, css, javascript (code -> request server) --> get dataexam


"""