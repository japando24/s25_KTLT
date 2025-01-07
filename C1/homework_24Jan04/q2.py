#Q2: Viết hàm chuẩn hóa chuỗi. Chuỗi được chuẩn hóa không chứa các khoảng trắng dư thừa, các từ cách nhau bởi một khoảng trắng.
#Demo

str0=input("Enter your string: ")
def q2(str):
    str=str.strip()
    while "  " in str:
        str=str.replace("  "," ")
    print(str)
while True:
    q2(str0)
