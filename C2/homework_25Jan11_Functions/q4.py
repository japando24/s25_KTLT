#Q4: Viết hàm tính tổng của n số hạng (sử dụng đệ quy và khử để quy).
def input_n():
    flag=False
    while not flag:
        try:
            n=int(input("Enter N: "))
            flag=True
        except ValueError:
            print("Please, enter only integers greater than 0!")
    return n

def sum_KDQ(n):
    res=0
    for i in range (1,n+1):
        res += i
    return res

def sum_DQ(n):
    if n==1:
        return 1
    else:
        return n+sum_DQ(n-1)

n=input_n()
print("NON-RECURSION")
print(f"Tổng của {n} số hạng: {sum_KDQ(n)}")
print("RECURSION")
print(f"Tổng của {n} số hạng: {sum_DQ(n)}")








