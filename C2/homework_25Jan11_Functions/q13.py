#Q13: Viết hàm tính tổng ước số để áp dụng chung cho 2 câu dưới đây:
# a) Kiểm tra số nguyên dương n có phải là số hoàn thiện (Pefect number) hay không? (Số hoàn thiện là số có tổng các ước số của nó (không kể nó) thì bằng chính nó.
# Vd: 6 có các ước số là 1,2,3 và 6=1+2+3➔6 là số hoàn thiện)
# b) Kiểm tra số nguyên dương n có phải là số thịnh vượng (Abundant number) hay không? (Số thịnh vượng là số có tổng các ước số của nó (không kể nó) thì lớn hơn nó.
# d: 12 có các ước số là 1,2,3,4,6 và 12<1+2+3+4+6➔12 là số thịnh vượng
def ip():
    flag=False
    while not flag:
        try:
            a=int(input("Enter check number: "))
            if a>0:
                flag=True
            else:
                print("Please, enter only integer number greater than 0!")
        except ValueError:
            print("Please, enter only integer number greater than 0!")
    return a

def sum_divisors(n,d=None):
    if d is None:
        d = n // 2

    if d == 0:  # Đk dừng, ko còn ước số nào để ktra
        return 0

    if n % d == 0:  # Nếu divisor là ước của n
        return d + sum_divisors(n, d - 1)
    else:
        return sum_divisors(n, d - 1)

def perfect_num(x):
    return True if sum_divisors(x) == x else False

def abundant_num(x):
    return True if sum_divisors(x) > x else False
x=ip()
if perfect_num(x):
    print(f"{x} is perfect number.")
else:
    print(f"{x} is NOT perfect number.")
if abundant_num(x):
    print(f"{x} is abundant number.")
else:
    print(f"{x} is NOT abundant number.")

