#Q6: Viết hàm tách họ, tên đệm và tên.
# Vd: với chuỗi họ tên “ Huynh nhat Nam Anh ” à Họ: Huynh, Tên đệm: Nhat Nam, Tên: Anh
#Demo

#str=" Huynh nhat Nam Anh "
def q6():
    str=input("Enter your fullname: ")
    str=str.strip().lower().title()
    list=str.split()
    l=len(list)
    middle=""
    for i in range (1,l-1):
        middle+=list[i] +" "

    print(f"First name: {list[0]}")
    print(f"Middle name: {middle.strip()}")
    print(f"Last name: {list[l-1]}")

while True:
    q6()
