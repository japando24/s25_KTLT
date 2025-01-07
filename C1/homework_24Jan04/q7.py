#Q7: Viết chương trình đảo ngược các từ trong chuỗi.
# Vd: “qua lại khách chờ sông lặng sóng” => “sóng lặng sông chờ khách lại qua”;
# “bèo trôi nước giợn sóng mênh mông” => “mông mênh sóng giợn nước trôi bèo”.
#Demo

#str="    qua     lại khách chờ sông    lặng sóng"
def q7():
    str = input("Enter the verse you want to invert: ")
    str = str.strip()
    while "  " in str:
        str = str.replace("  ", " ")
    list = str.split(" ")
    list.reverse()
    res = ""
    for i in list:
        res = res + i + " "
    print(res.strip())

while True:
    q7()