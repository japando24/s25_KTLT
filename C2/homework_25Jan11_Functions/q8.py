#Q8: Viết hàm (sử dụng đệ quy và khử để quy) tính biểu thức sau:
import math
def ip():
    flag=False
    while not flag:
        try:
            a=int(input("Enter number: "))
            flag=True
        except ValueError:
            print("Please, enter only integer number!")
    return a

def q8_kdq(x,n):
    s=0
    for i in range (1,n+1):
        s += (x**n)/math.factorial(n)
    return s

def q8_dq(x,n):
    if (x==0 and n==1):
        return 0
    elif (x==0 and n==0) or (x==1 and n==0) or (x==1 and n==1):
        return 1
    else:
        return (x**n)/math.factorial(n) + q8_dq(x,n-1) if n>0 else False

print("x")
x=ip()
print("n")
n=ip()
print("-"*30)
print("NON-RECURSION")
print(f"Result of expression: {q8_kdq(x,n)}")
print("RECURSION")
print(f"Result of expression: {q8_dq(x,n)}")


