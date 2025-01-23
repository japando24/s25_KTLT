#Q2: Viết hàm chuyển đổi năm dương lịch sang âm lịch với tên gọi Can + Chi
# (ví dụ: Năm 2021 là Tân Sửu).
"""
Cơ sở lý thuyết:
10 Thiên Can: Giáp, Ất, Bính, Đinh, Mậu, Kỷ, Canh, Tân, Nhâm, Quý
12 Địa Chi (12 Con Giáp): Tý, Sửu, Dần, Mão, Thìn, Tỵ, Ngọ, Mùi, Thân, Dậu, Tuất, Hợi
VD: 1960: Canh Tý
"""
ThienCan={0:"Canh", 1:"Tân", 2:"Nhâm", 3:"Quý", 4:"Giáp",
          5:"Ất", 6:"Bính", 7:"Đinh", 8:"Mậu", 9:"Kỷ"}
#Lấy năm chia cho 12, phần dư tra bảng
DiaChi={0:"Thân", 1:"Dậu", 2:"Tuất", 3:"Hợi", 4:"Tý", 5:"Sửu",
        6:"Dần", 7:"Mão", 8:"Thìn", 9:"Tỵ", 10:"Ngọ", 11:"Mùi"}
def chinese_calendar(y):
    y_digits=[int(d) for d in str(y)]
        # y_digits=[]
        # for d in str(y):
        #     y_digits.append(d)
    l=len(y_digits)
    tc=ThienCan[int(y_digits[l-1])]
    dc=DiaChi[int(y%12)]
    print(f"Năm {y} là {tc} {dc}")
def input_year():
    flag=False
    while not flag:
        try:
            y=int(input("Nhập năm muốn tra cứu: "))
            flag=True
        except ValueError:
            print("Sai định dạng! Vui lòng nhập lại năm!")
    return y

while True:
    y=input_year()
    chinese_calendar(y)
    print("-"*50)

