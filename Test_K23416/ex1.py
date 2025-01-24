#%% - Import Lib
import json

import requests

# - Get data
url = "https://fakestoreapi.com/products"
response = requests.get(url)

# Display data
products = response.json()
print(products)

# Save data
with open("data/products.json","w",encoding="utf8") as f:
    json.dump(products, f,indent=3)
