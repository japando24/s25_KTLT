#Câu 1: Viết phương thức với đối số đầu vào là số có tối đa 2 chữ số. Hãy in ra cách đọc số bằng tiếng Anh
# (ví dụ đọc số: 5: five, 11: eleven, 12: twelve, 15: fifteen, 20: twenty, 35: thirty-five; 55: fifty-five; ….).

print("HOW TO READ NUMBER IN ENGLISH")
print("-"*25)

def input_number():
    flag=False
    while not flag:
        try:
            my_number=int(input("Enter number (0-99): "))
            if 0<=my_number<=99:
                flag=True
            else:
                print("Please, enter a positive number!")
        except ValueError:
            print("Please, enter a positive integer!")
    return my_number

one_digit_unit= {
    "0" : "zero",
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine"
}

one_digit_tens={
    "0" : "ty",
    "1" : "teen",
    "2" : "twen",
    "3" : "thir",
    "5" : "fif",
    "6" : "six",
    "7" : "seven",
    "8" : "eigh",
    "9" : "nine"
}
def read_number_en(n):
    n_str=str(n)
    n_length=len(n_str)
    if n_length==1:
        return (f"{n}  ==> {one_digit_unit[n_str]}")
    else:
        if n==10:
            return (f"{n} ==> ten")
        elif n==11:
            return (f"{n} ==> eleven")
        elif n==12:
            return (f"{n} ==> twelve")
        elif n==14:
            return (f"{n} ==> fourteen")
        elif n==40:
            return (f"{n} ==> forty")
        else:
            if n % 10 == 0:
                return f"{n} ==> {one_digit_tens[n_str[0]]}ty"
            elif n%40 != 0 and 40<=n<=49:
                return f"{n} ==> forty {one_digit_unit[n_str[1]]}"
            elif n-10!=0 and 13<=n<=19: #13, 15, 16, 17, 18, 19
                return f"{n} ==> {one_digit_tens[n_str[1]]}teen"
            else:
                return f"{n} ==> {one_digit_tens[n_str[0]]}ty {one_digit_unit[n_str[1]]}"





n=input_number()
print(read_number_en(n))
