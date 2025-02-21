#%%
import requests
import xml.etree.ElementTree as ET
url = "https://fakestoreapi.com/products"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
root = ET.Element("e1b1")

#%%
import requests
import xml.etree.ElementTree as ET
url = "https://fakestoreapi.com/products"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    root = ET.Element("e1a")
    for item in data:
        product = ET.SubElement(root, "product")
        ET.SubElement(product, "id").text = str(item["id"])
        ET.SubElement(product, "title").text = item["title"]
        ET.SubElement(product, "description").text = item["description"]
        ET.SubElement(product, "category").text = item["category"]
        ET.SubElement(product, "image").text = item["image"]
        rating = ET.SubElement(product, "rating")
        rating.set("race", str(item["rating"]["rate"]))
        rating.set("count", str(item["rating"]["count"]))

    tree = ET.ElementTree(root)
    with open("exam14022025/dataexam/e1b2.xml", "wb") as file:
        tree.write(file, encoding="utf-8", xml_declaration=True)

    print("Dữ liệu đã được lưu vào 'e1b2.xml'")
else:
    print(f"Lỗi: {response.status_code}")