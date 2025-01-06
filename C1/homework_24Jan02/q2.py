#Q2: Viết hàm kiểm tra 2 từ (tiếng Anh) có phải được tạo thành bằng cách sắp xếp lại các chữ cái của từ còn lại.
# Ví dụ: “cinema” – “iceman”, “tea” – “eat”, “care” – “race”, “dad” – “add”, “medical” – “decimal” => True.
#Demo
str1="  cinema   "
str2="  iceman    "
str1=str1.lower().strip(" ")
str2=str2.lower().strip(" ")

if len(str1) != len(str2):
    print("These two words have NO relationship.")
else:
    l=len(str1)
    list1=list(str1)
    list2=list(str2)
    count=0
    for i in list1:
        for j in list2:
            if i == j:
                count +=1
            else:
                continue
    if count == l:
        print("These two words can be arranged to make the remaining word.")
    else:
        print("These two words have NO relationship.")



