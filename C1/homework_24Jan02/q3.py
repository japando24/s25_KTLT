#Q3: Viết hàm tìm chuỗi con chung dài nhất trong 2 chuỗi cho trước. Ví dụ: “qwert” – “hqwersvj” -> “qwer”.
#Demo
#Test case 1: cụm
# str1="qwert"
# str2="hqwersvj"
#Test case 2: câu
str1="Mom goes to market I go to school"
str2="I go to school"

str1=str1.strip(" ")
str2=str2.strip(" ")
#TH1: Cụm
if len(str1.split(" ")) == len(str2.split(" ")) == 1:
    list1 = list(str1)
    list2 = list(str2)
# TH2: Câu
else:
    list1 = str1.split(" ")
    list2 = str2.split(" ")
#Độ dài
len1=len(list1)
len2=len(list2)
#Xác định chuỗi ngắn làm main string
if len1 <= len2:
    len_min=len1
    len_max=len2
    list_min=list1
    list_max=list2
else:
    len_min = len2
    len_max = len1
    list_min=list2
    list_max=list1
res=""
for i in range (len_min):
    for j in range (len_max):
        if list_min[i] == list_max[j]:
            if len(str1.split(" ")) == len(str2.split(" ")) == 1:
                res+=str(list_min[i])
            else:
                res = res + str(list_min[i]) + " "
        else:
            continue
print(res.strip())






