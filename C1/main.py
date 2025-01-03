# # from C1.func import count_c_max
from C1.func import count_c_max, my_join, chuan_hoa, process_s_3

print("*"*30)
print("1. Liệt kê các ký tự có tần suất xuất hiện nhiều nhất:")
print("2. Gộp các phần tử của list -> chuỗi (join - buil-in function)")
print("3. Gộp các phần tử của list -> chuỗi (join - self build-in)")
print("4. Chuẩn hóa chuỗi 1")
print("5. Chuẩn hóa chuỗi 2")
print("0. Thoát chương trình")
print("*"*30)

while True:
    c=input("Chọn chức năng muốn thực hiện:")
    org_s = input("Nhập chuỗi: ")
    match c:
        case "1":
            res,count=count_c_max(org_s)
            print(f"{res} xuất hiện nhiều nhất {count} lần")
        case "2":
            beers=org_s.split(", ")#['Tiger,', 'Heineken,', 'Sapporo']
            #beers1=list(s) #['T', 'i', 'g', 'e', 'r', ',', ' ', 'H', 'e', 'i', 'n', 'e', 'k', 'e', 'n', ',', ' ', 'S', 'a', 'p', 'p', 'o', 'r', 'o']
            #Duyê ds
            for b in beers:
            #Gộp các phần tử của ds => chuỗi
                merge_s=" * ".join(beers)
            print(merge_s)
        case "3":
            print(my_join(org_s," %%% "))
        case "4":
            print(chuan_hoa(org_s))
        case "5":
            print(process_s_3())
        case _:
            print("じゃあね（Jaane)!")
            break


