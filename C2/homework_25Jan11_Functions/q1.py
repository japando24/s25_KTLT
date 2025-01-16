#Q1: Viết hàm kiểm tra năm nhuận.
"""
Cơ sở lý thuyết:
Năm nhuận khi:
+ Chia hết cho 4 và ko chia hết cho 100
+ Chia hết cho 400
"""

def input_year():
    flag=False
    while not flag:
        try:
            y=int(input("Nhập năm muốn kiểm tra: "))
            flag=True
        except ValueError:
            print("Sai định dạng! Vui lòng nhập lại năm!!!")
    return y

def leap_year(y):
    if (y%4 == 0 and y%100 != 0) or y%400 == 0:
        print(f"Năm {y} là năm nhuận.")
    else:
        print(f"Năm {y} KHÔNG phải năm nhuận.")

while True:
    y=input_year()
    leap_year(y)
    print("-"*50)

