# f=open("data/test.txt","w",encoding="utf-8")
# f.write("Qua lại \n")
# f.write("Sóng \n")
# f.close()
#%%
#a: append: ghi nối tiếp
#w: write: ghi đè

from func import *
content = """Welcome to UEL
Welcome to UEL
"""
s="Hello..."
# save_txt("data/test.txt","a",s)
# save_txt_2("data/test2.txt","a",s)

#Read Data 1
# f=open("data/test.txt","r",encoding="utf-8")
# for line in f:
#     print(line.strip().upper())

with open("data/test.txt","r",encoding="utf-8") as f:
    print(f.read().upper())



