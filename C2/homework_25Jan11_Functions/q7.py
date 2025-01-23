#Q7: Viết hàm (sử dụng đệ quy và khử để quy) tính biểu thức sau:
def input_n():
    flag=False
    while not flag:
        try:
            n=int(input("Enter N: "))
            flag=True
        except ValueError:
            print("Please, enter only integers greater than 0!")
    return n

def q7_KDQ(n):
    denominator=0
    res=0
    for i in range (1,n+1):
        denominator += i
        res += 1/denominator
    return res

def q7_DQ(n):
    if n==1:
        return 1
    else:
        return 1/sum(range(1,n+1)) + q7_KDQ(n-1)

n=input_n()
print("NON-RECURSION")
print(f"Result of expression with n={n}: {q7_KDQ(n)}")
print("RECURSION")
print(f"Result of expression with n={n}: {q7_DQ(n)}")
