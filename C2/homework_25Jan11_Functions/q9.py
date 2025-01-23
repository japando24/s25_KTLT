#Q9: Viết hàm (sử dụng đệ quy và khử để quy) tính biểu thức sau:
def ip():
    flag=False
    while not flag:
        try:
            a=int(input("Enter number: "))
            flag=True
        except ValueError:
            print("Please, enter only integer number!")
    return a
def q9_kdq(n):
    s=0
    for i in range (n+1):
        s += ((2*i+1)/(2*i+2))
    return s

def q9_dq(n):
    if n==0:
        return 0.5
    else:
        return ((2*n+1)/(2*n+2)) + q9_dq(n-1) if n>0 else False

print("n")
n=ip()
print("NON-RECURSION")
print(f"Result of expression with n={n}: {q9_kdq(n)}")
print("RECURSION")
print(f"Result of expression with n={n}: {q9_dq(n)}")
