#Q1: Viết hàm nhận đầu vào một chuỗi bất kỳ và in ra tần suất của mỗi từ theo thứ tự giảm dần, không xét khoảng trống và dấu câu.
#Demo
str="    Japan    Do is BanGenji.    LOVELY LOVELY!   "
# #Bỏ khoảng trắng đầu cuối
# str=str.strip()
# #Bỏ khoảng trắng giữa
# while "  " in str:
#     str=str.replace("  "," ").replace(" ","")
s_list = list(str)
s_new_list = []
for i in range(len(s_list)):
    if s_list[i].isalnum():
        s_new_list.append(s_list[i].lower())
#Bỏ ký tự trùng
s_list_only=set(s_new_list)
print(s_list_only)
dic={}
for c in s_list_only:
    dic[c] = [1, False]
for c in s_new_list:
    if dic[c][1] == False:
        dic[c][1] = True
    else:
        dic[c][0] += 1
print(dic)