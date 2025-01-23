#Q6: Viết hàm (sử dụng đệ quy và khử để quy) tính biểu thức sau:
def ip():
    flag=False
    while not flag:
        try:
            a=int(input("Enter number: "))
            flag=True
        except ValueError:
            print("Please, enter only integers greater than 0!")
    return a
def q6_kdq(x,n):
    s=0
    for i in range(1,n+1):
        s +=  x**(2*i)
    return s

def q6_dq(x,n):
    if n==1:
        return x**2
    return x**(2*n) + q6_dq(x,n-1)

print("x")
x=ip()
print("n")
n=ip()
print("-"*30)
print("NON-RECURSION")
print(f"Result of expression: {q6_kdq(x,n)}")
print("RECURSION")
print(f"Result of expression: {q6_dq(x,n)}")
