#%% Import Lib
import json

import xmltodict as xm

#%% Convert xml --> json
with open("data/products.xml","r",encoding="utf8") as f:
    json_obj = xm.parse(f.read())
    #temp = json.dumps(json_obj, indent=3) # biến đổi json sang chuỗi (ko dùng để truy xuất)
    #print(json_obj["products"]["product"])
    #Save data (json file)
with open("data/beers.json","w",encoding="utf8") as json_f:
    json.dump(json_obj["products"]["product"],json_f,indent=3)