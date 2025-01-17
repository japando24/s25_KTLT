#Q10: Viết hàm tính chỉnh hợp, tổ hợp chập k của n phần tử
# (sử dụng kỹ thuật đệ quy tính giai thừa cho hàm xử lý trung gian).
"""
Cơ sở lý thuyết:
Chỉnh hợp (permutation): nAm = n!/(n-m)! (ĐK: n >= m > 0)
Tổ hợp (combination): nCm = n!/(m!*(n-m)!) (ĐK: n >= m > 0)
"""
def ip():
    flag=False
    while not flag:
        try:
            a=int(input("Enter number: "))
            if a>0:
                flag=True
            else:
                print("Please, enter only integer number greater than 0!")
        except ValueError:
            print("Please, enter only integer number greater than 0!")
    return a

def factorial(f):
    if f == 1 or f == 0:
        return 1
    else:
        return f*factorial(f-1) if f>=0 else False
def permutation(n,m):
    A=factorial(n)/factorial(n-m)
    return A
def combination(n,m):
    C=permutation(n,m)*(1/factorial(m))
    #C=factorial(n)/(factorial(m)*factorial(n-m)
    return C

flag1=False
while not flag1:
    print("MENU")
    print("1. Permutation (Chỉnh hợp)")
    print("2. Combination (Tổ hợp)")
    print("0. EXIT")
    pick=int(input("Choose function: "))
    if pick == 1:
        print("n of nAm")
        n=ip()
        print("m of nAm")
        m=ip()
        while n<m:
            print("Please, enter n>=m!")
            print("n of nAm")
            n = ip()
            print("m of nAm")
            m = ip()
        print(f"Permutation of {n} choose {m}: {permutation(n, m)}")
        print("*" * 50)
    elif pick == 2:
        print("n of nCm")
        n = ip()
        print("m of nCm")
        m = ip()
        while n < m:
            print("Please, enter n>=m!")
            print("n of nCm")
            n = ip()
            print("m of nCm")
            m = ip()
        print(f"Combination of {n} choose {m}: {combination(n, m)}")
        print("*"*50)
    elif pick == 0:
        print("THANK YOU FOR USING! LOVE LOVE")
        break
    else:
        print("Please, choose right number in menu!")
        print("*" * 50)





