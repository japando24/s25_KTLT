from xml.dom.minidom import parse
tree = parse("data/ptoduct.xml")
elements = tree.documentElement

product_elements = elements.getElementsByTagName("product")
#print (product_elements)
for p in product_elements:
    code = p.getElementsByTagName("code")[0].childNodes[0].data
    name = p.getElementsByTagName("name")[0].childNodes[0].data
    price = p.getElementsByTagName("price")[0].childNodes[0].data
    print(f"{code}: {name} -- {price} VNĐ")
"""
Explain:
1. p=0
vị trí code số 0
childNotes vị trí con đầu tiên
VD: <code> 1
"""
