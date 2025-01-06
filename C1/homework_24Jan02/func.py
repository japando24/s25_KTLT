def q1():
    str=input("Enter the string you want to check: ")
    #Băm chuỗi
    s_list=list(str)
    #Loại bỏ khoảng trống và ký tự khác ngoài chữ và số
    s_list1=[]
    for i in range (len(s_list)):
        if s_list[i].isalnum():
            s_list1.append(s_list[i].lower())
    #Bỏ ký tự trùng
    s_list_unique=set(s_list1)
    #Sử dụng Dictionary
    dic={}
    for c in s_list_unique:
        dic[c]=[1,False]
    for key in s_list1:
        if dic[key][1] == False:
            dic[key][1]=True
        else:
            dic[key][0]+=1
    list_key=dic.keys()
    print("Frequency of occurrence of characters in your string:")
    sort_dic1=sorted(dic.items(), key=lambda item: item[1][0], reverse=True)
    for item in sort_dic1:
        key=item[0]
        value=item[1][0]
        print(f'{key}: {value}-time')

def q2():
    word1 = input("Enter 1st word: ")
    word2 = input("Enter 2nd word: ")
    word1=word1.lower().strip(" ")
    word2=word2.lower().strip(" ")
    #So sánh độ dài 2 chuỗi
    if len(word1) != len(word2):
        print("These two words have NO relationship.")
    else:
        #Băm chuỗi để so sánh
        l = len(word1)
        list1 = list(word1)
        list2 = list(word2)
        count = 0
        #So sánh từng ký tự
        for i in list1:
            for j in list2:
                if i == j:
                    count += 1
                else:
                    continue
        if count == l:
            print("These two words can be arranged to make the remaining word.")
        else:
            print("These two words have NO relationship.")

def q3():
    str1=input("Enter the 1st string: ")
    str2=input("Enter the 2nd string: ")
    str1 = str1.strip(" ")
    str2 = str2.strip(" ")
    # TH1: Cụm
    if len(str1.split(" ")) == len(str2.split(" ")) == 1:
        list1 = list(str1)
        list2 = list(str2)
    # TH2: Câu
    else:
        list1 = str1.split(" ")
        list2 = str2.split(" ")
    # Độ dài
    len1 = len(list1)
    len2 = len(list2)
    # Xác định chuỗi ngắn làm main string
    if len1 <= len2:
        len_min = len1
        len_max = len2
        list_min = list1
        list_max = list2
    else:
        len_min = len2
        len_max = len1
        list_min = list2
        list_max = list1
    res = ""
    for i in range(len_min):
        for j in range(len_max):
            if list_min[i] == list_max[j]:
                if len(str1.split(" ")) == len(str2.split(" ")) == 1:
                    res += str(list_min[i])
                else:
                    res = res + str(list_min[i]) + " "
            else:
                continue
    return res.strip()
def q4():
    str=input("Enter the string you want to check: ")
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
        s_list0 = {
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
        print("Characters absent from this string: ", end="")
        res = ""
        for key in s_list0:
            if not s_list0[key]:
                res += key + ", "
        res = res.rstrip(", ")
        print(res, end="")
