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
    for key in list_key:
        print(f'{key}: {dic[key][0]}-time')

def q2():
    pass
def q3():
    pass
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
