import xml.etree.ElementTree as ET
tree=ET.parse("data/product2.xml")
root=tree.getroot()
"""
print(root.tag) #products
print(root.attrib) # {'name': 'product-list'}

for child in root:
    print(child.tag)
    # product
    # product
    # product
"""

print(root[1][1].text) #Blanc 1664

#Duyệt qua các thẻ "product"
for p in root.iter("product"): #Quét toàn bộ
    #print(f"{p[0].text}: {p[1].text} -- {p[2].text}") #Cách 1
    #print(f"{p.find('code').text}: {p.find('name').text} -- {p.find('price').text}")  #Cách 2: find là lấy tên thẻ
    print(f"{p.get('pCode')}: {p.find('name').text} -- {p.find('price').text}")  #Cách 3: get là lấy thuộc tính
print("-"*30)

# for p in root.findall("product"):
#     print(p.tag)

# for s in root,iter("slogan"):
#     s.text=s.text.upper()
# tree.write("data/product_2_updated.xml",encoding="utf-8")

for p in root.iter("product"):
    p.find("price").text="$" + str(float(p.find("price").text) /25000)
tree.write("data/product2_update.xml",encoding="utf-8")

