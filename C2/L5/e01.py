#Tính tổng n số hạng: dùng đệ quy và khử đệ quy
#C1: Khử đệ quy
def tong1(n):
    t=1
    i=2
    while i<= n:
        t += i
        i+=1
    return t

def tong2(n):
    return n*(n+1)/2

#C2: Dùng đệ quy
#Xđ được quy luật và điểm dừng
def tong11(n):
    if n==0 or n==1:
        return n
    else:
        return n + tong11(a-1)

def tong3(n):
    return 1 if n==1 else n + tong3(n-1)

print(tong3(3))