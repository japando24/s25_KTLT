def count_c_max(s):
    org_s=s.lower()
    out_s = ""
    count_max = 0
    res_s = ""
    for c in org_s:
        if c != " " and c not in out_s:
            out_s += c
    for c in out_s:
        count = org_s.count(c)
        if count > count_max:
            count_max = count
            res_s = c + ","
        elif count == count_max:
            res_s += c + ","
    return res_s.rstrip(","), count_max


def my_join(lst, s):
    res = ""
    for item in lst:
        res += item + s
    return res.rstrip(s)

"""
HOMEWORK
Định nghĩa hàm "Chuẩn hóa chuỗi"
loại bỏ khoảng trắng dư thừa trong chuỗi
VD: "     kHoa    he    thong    tHong tin  " => "Khoa He Thong Thong Tin"
"""
def chuan_hoa(org_s):
    list=org_s.title().split()
    edit_s=" ".join(list)
    return edit_s

# s="      "
# s=s.strip()
# while True:
#     if s.find("  ") != -1:
#         s=s.replace("  "," ")
#     else:
#         break
# print(s.title())

def process_s(s):
    s=s.strip()
    # Trong khi còn tìm thấy 2 khoảng trắng liên tiếp -> thay thế bằng 1 khoảng trắng
    # while s.count("  ") != 0:
    # while s.find("  ") != -1:
    while "  " in s:
        s=s.replace("  "," ")
    return s.title()
def process_s_2(s):
    s=s.split()
    return " ".join(s)

def process_s_3(s):
    s= "    kHoa    he    thong    tHong tin"
    s=s.strip()
    res=""
    i = 0
    l=len(s)
    while i < l:
        if s[i] != " ":
            res += s[i]
        elif s[i] == " " and s[i-1] != " ":
            res += " "
        i +=1
    return res.title()

s="---8whdg-8bhl----68p8e--h-----0000hfhg---" #==> -8 -68
res=""
l=len(s)
i=0
while i<l:
    if s[i] == "-" and s[i+1].isdigit():
        j = i+2
        while j<l:
            if not s[j].isdigit():
                break
        if j != i+2:
            res += "-" + s[i:j]
    return res



