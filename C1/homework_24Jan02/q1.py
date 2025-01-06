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
print(f's_list_only: {s_list_only}')
dic={}
for c in s_list_only:
    dic[c] = [1, False]
for c in s_new_list:
    if dic[c][1] == False:
        dic[c][1] = True
    else:
        dic[c][0] += 1
#Sắp xếp theo thứ tự giảm dần
print(f'dic: {dic}')
test=dic.items()
print(f'test: {test}')
sort_dic=sorted(dic.items(), key=lambda item: item[1][0], reverse=True)
print(f'sort_dic: {sort_dic}')
for item in sort_dic:
    key=item[0]
    value = item[1][0]
    print(f'Key: {key}, Value: {value}')

#BÀI TOÁN MỞ RỘNG: Sau khi sắp xếp theo thứ tự giảm dần theo số lần
# thì sắp xếp đồng cấp theo alphabet và number (tăng dần: A=>Z, 0=>9)
#Thingking...


