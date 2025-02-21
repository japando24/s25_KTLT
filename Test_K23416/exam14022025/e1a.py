#%% IMPORT LIBRARY
import json
import requests


#%% GET DATA
url= "https://fakestoreapi.com/products"
response=requests.get(url)
if response.status_code == 200:
    data = response.json()

#%% SAVE DATA - a
with open ("dataexam/data_e1a.json","w",encoding="utf8") as f:
    json.dump(data,f,ensure_ascii=False,indent=4)



