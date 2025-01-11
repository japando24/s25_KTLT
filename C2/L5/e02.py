#Q5: Viết hàm tìm UCLN của 2 số (dùng kỹ thuật đệ quy và khử đệ quy)
# a=8
# b=24
# u=0
#
# def UCLN1(a,b):
#     small=0
#     big=0
#     if a<b:
#         big=b
#         small=a
#     elif a>b:
#         big=a
#         small=b
#
#     du=big%small
#     if small==0:
#         return big
#     while du != 0:
#         res=du
#         du=small%du
#         small=res
#     return small
# a=int(input("Nhập số nguyên ko âm: "))
# b=int(input("Nhập số nguyên ko âm: "))
# print(UCLN1(a,b))
#Khoảng cách quá lớn: chia lấy dư
#Khoảng cách nhỏ: dùng cách nào cũng được
def UCLN_C1(a,b):
    while a*b !=0:
        if a>b:
            a=a%b
        else:
            b%=a
    print(f"UCLN: {a+b}")

def UCLN_C2(a,b):
    if a*b==0:
        return a+b
    else:
        return UCLN_C2(a%b, b) if a>b else UCLN_C2(a,b%a)