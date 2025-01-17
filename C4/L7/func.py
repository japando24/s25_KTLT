def save_txt(path, mode, content):
    f=open(path, mode, encoding="utf-8")
    f.write(content)
    f.close()
def save_txt_2(path, mode, content):
    with open("data/test2.txt","w",encoding="utf-8") as f:
        f.write(content)