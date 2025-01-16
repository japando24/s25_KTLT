#Q3: Viết hàm kiểm tra một số có phải là số nguyên tố, số chính phương
"""
Cơ sở lý thuyêt:
Số nguyên tố: chỉ chia hết cho 1 và chính nó
Số chính phương: căn bậc của n * căn bậc hai của n = n
"""
from math import sqrt


def input_number():
    flag=False
    while not flag:
        try:
            x=int(input("Nhập số muốn kiểm tra: "))
            flag=True
        except ValueError:
            print("Vui lòng chỉ nhập số nguyên!")
    return x

def snt(x):
    if x<2:
        return False
    else:
        for i in range (2,int(sqrt(x))+1,):
            if x%i == 0:
                return False
        return True

def scp(x):
    if int(x)<0:
        return False
    return int(int(x)**0.5)**2 == int(x)

print("MENU")
print("1. Kiểm tra số nguyên tố.")
print("2. Kiểm tra số chính phương.")
print("0. THOÁT")
print("-"*50)
pick=int(input("Chọn chức năng: "))
while True:
    if pick == 1:
        x=input_number()
        if snt(x) == False :
            print(f"Số {x} là KHÔNG số nguyên tố.")
        else:
            print(f"Số {x} là số nguyên tố.")
        print("*"*50)
    elif pick == 2:
        x=input_number()
        if snt(x) == False:
            print(f"Số {x} là KHÔNG số chính phương.")
        else:
            print(f"Số {x} là số chính phương.")
        print("*"*50)
    elif pick == 0:
        print("Thank you!!!")
        break
    else:
        print("Vui lòng chỉ nhập số theo chức năng!")






