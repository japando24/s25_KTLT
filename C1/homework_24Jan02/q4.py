#Q4: Viết hàm kiểm tra xem 1 câu (tiếng Anh) có chứa mọi chữ cái trong bảng chữ cái ít nhất một lần.
# Ví dụ: “The job requires extra pluck and zeal from every young wage earner.” => True.
#Demo

#Test Case
# str="The job requires extra pluck and zeal from every young wage earner." ==> True
str = "Japan Do is YouTuber BanGenji. Thank you for watching!!!"

#THỎA YÊU CẦU BÀI TOÁN:
s_list1=list(str)
s_list2=[]
for i in range (len(s_list1)):
    if s_list1[i].isalnum():
        s_list2.append(s_list1[i].lower())
s_list2=set(s_list2)
if len(s_list2) == 26: #Bảng chữ cái TA có 26 chữ cái
    print("This string has fully enough 26 English characters.")
else:
    print("This string has NOT fully enough 26 English characters.")

#MỞ RỘNG BÀI TOÁN: Khi đã xác định là KO đủ 26 chữ cái thì cần xuất ra những chữ cái còn thiếu
s_list1=list(str)
s_list2=[]
for i in range (len(s_list1)):
    if s_list1[i].isalnum():
        s_list2.append(s_list1[i].lower())
s_list2=set(s_list2)
s_list0={
    "a": False,
    "b": False,
    "c": False,
    "d": False,
    "e": False,
    "f": False,
    "g": False,
    "h": False,
    "i": False,
    "j": False,
    "k": False,
    "l": False,
    "m": False,
    "n": False,
    "o": False,
    "p": False,
    "q": False,
    "r": False,
    "s": False,
    "t": False,
    "u": False,
    "v": False,
    "w": False,
    "x": False,
    "y": False,
    "z": False,
}
for i in s_list2:
    if s_list0[i] == False:
        s_list0[i] = True
print("Các ký tự không có trong chuỗi: ", end="")
res = ""
for key in s_list0:
    if not s_list0[key]:
        res += key + ", "
res = res.rstrip(", ")
print(res,end="")