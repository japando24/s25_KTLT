#%%
import requests
import json
from bs4 import BeautifulSoup
url = "https://vnexpress.net/the-gioi"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
items = soup.find_all("article", class_="item-news")
articles = []
for item in items:
    try:
        tieu_de= item.find("h3").text
        tom_tat = item.find("p", class_="description").text
        articles.append({
        "tieu de": tieu_de,
        "tom tat": tom_tat
         })
    except:
     continue
with open("exam14022025/dataexam/data_e3.json", "w", encoding="utf-8") as f:
    json.dump(articles, f, indent=4, ensure_ascii=False)