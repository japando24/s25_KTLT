#Câu 2: Viết phương thức đọc số tự nhiên có tối đa 3 chữ số,
# ví dụ: 11 à “Mười một”, 21 à “Hai mươi mốt”, 201 à “Hai trăm linh một”, 65 à “Sáu mươi lăm”, 305 à “Ba trăm linh năm”, ….
print("HOW TO READ NUMBER IN VIETNAMESE")
print("-"*25)
#Hàm tạo vòng lặp, để cho việc nhập số đúng giá trị.
def input_number():
    flag=False
    while not flag:
        try:
            n_f=int(input("Enter number (0-999): "))
            if n_f<1000:
                flag=True
            else:
                print("Please, enter number again! The number only has form 1 to 3 digit")
        except ValueError:
            print("Please, enter number again! Invalid value.")
    return n_f
#vô chi tiết cách đọc số theo tiếng Việt
one_digit = {
    "0" : "không",
    "1" : "một",
    "2" : "hai",
    "3" : "ba",
    "4" : "bốn",
    "5" : "năm",
    "6" : "sáu",
    "7" : "bảy",
    "8" : "tám",
    "9" : "chín"
}
#đưa số về dạng chuỗi

def read_number(n):
    n_str = str(int(n))
    #n_list = list(n_str)
    n_length = len(n_str)
    if n_length==1:
        return f"{n} ==> {one_digit[n_str]}"
    elif n_length==2: #TH: 20, 21, 24, 25, (23)
        if n_str[0] == "1" and n_str[1]=="0":
            return(f"{n} ==> mười")
        elif n!="10" and int(n)%10==0:
            return(f"{n} ==> {one_digit[n_str[0]]} mươi")
        else:
            if n_str[0] == "1" and n_str[1] == "5":
                return (f"{n} ==> mười lăm")
            elif n_str[0] == "1":
                return (f"{n} ==> mười {one_digit[n_str[1]]}")
            elif n_str[1] == "1":
                return (f"{n} ==> {one_digit[n_str[0]]} mươi mốt")
            elif n_str[1] == "4":
                return (f"{n} ==> {one_digit[n_str[0]]} mươi tư")
            elif n_str[1] == "5":
                return (f"{n} ==> {one_digit[n_str[0]]} mươi lăm")
            else:
                return (f"{n} ==> {one_digit[n_str[0]]} mươi {one_digit[n_str[1]]}")
    else:
        if n_str[1] == "0":
            if n_str[2] == "0":
                return (f"{n} ==> {one_digit[n_str[0]]} trăm")
            else:
                return (f"{n} ==> {one_digit[n_str[0]]} trăm lẻ {one_digit[n_str[2]]}")
        else:
            if n_str[1] == "1" and n_str[2] == "0":
                return (f"{n} ==> {one_digit[n_str[0]]} trăm mười")
            elif n % 10 == 0:
                return (f"{n} ==> {one_digit[n_str[0]]} trăm {one_digit[n_str[1]]} mươi")
            else:
                if n_str[1] == "1" and n_str[2] == "5":
                    return (f"{n} ==> {one_digit[n_str[0]]} trăm mười lăm")
                elif n_str[1] == "1":
                    return (f"{n} ==> {one_digit[n_str[0]]} trăm mười {one_digit[n_str[2]]}")
                elif n_str[2] == "1":
                    return (f"{n} ==> {one_digit[n_str[0]]} trăm {one_digit[n_str[1]]} mươi mốt")
                elif n_str[2] == "4":
                    return (f"{n} ==> {one_digit[n_str[0]]} trăm {one_digit[n_str[1]]} mươi tư")
                elif n_str[2] == "5":
                    return (f"{n} ==> {one_digit[n_str[0]]} trăm {one_digit[n_str[1]]} mươi lăm")
                else:
                    return (f"{n} ==> {one_digit[n_str[0]]} trăm {one_digit[n_str[1]]} mươi {one_digit[n_str[2]]}")




n=input_number()
print(read_number(n))

for i in range (0,1000):
    print(read_number(i))