#%% - Import Lib
import json

import requests

# - Get dataexam
url = "https://fakestoreapi.com/products"
response = requests.get(url)

# Display dataexam
products = response.json()
print(products)

# Save dataexam
with open("data/products.json","w",encoding="utf8") as f:
    json.dump(products, f,indent=3)
