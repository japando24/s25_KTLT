def save_txt(path, mode, content):
    f=open(path, mode, encoding="utf-8")
    f.write(content)
    f.close()