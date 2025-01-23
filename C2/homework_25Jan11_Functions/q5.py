#Q5: Viết hàm tìm ước số chung lớn nhất của 2 số (dùng kỹ thuật đệ quy và khử đệ quy).

def input_num():
    flag=False
    try:
        x=int(input("Nhâp số nguyên dương: "))
    except ValueError:
        print("Vui lòng chỉ nhập số nguyên dương!")
    return x
def UCLN_KĐQ(a,b):
    while a*b !=0:
        if a>b:
            a=a%b
        else:
            b%=a
    print(f"UCLN: {a+b}")

def UCLN_ĐQ(a,b):
    if a*b==0:
        return a+b
    else:
        return UCLN_ĐQ(a%b, b) if a>b else UCLN_ĐQ(a,b%a)

print("Số thứ nhất")
a=input_num()
print("Số thứ hai")
b=input_num()
print("-"*30)
print("Khử Đệ Quy")
UCLN_KĐQ(a,b)
print("Đệ Quy")
res=UCLN_ĐQ(a,b)
print(f"UCLN: {res}")

