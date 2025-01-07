#Q4: Viết hàm xử lý trả về tên và phần mở rộng của tập tin. Hàm nhận đối số đầu vào là đường dẫn của tập tin.
#Vd: với đường dẫn “D:\\learning\python\string.py” à hàm sẽ trả về tên tập tin là “string” và phần mở rộng là “py”.
#Demo
import os

file_path=r"D:\\learning\python\string.py"
# file_path=input("Enter your file path: ")

#Solution 1:
print("Solution 1")

def q4_1(file_path):
    file_name, file_extension= os.path.splitext(os.path.basename(file_path))
    file_extension = file_extension[1:] #Bỏ dấu chấm
    return file_name, file_extension

file_name, file_extension = q4_1(file_path)
print(f"File Name: {file_name}")
print(f"File Extension: {file_extension}")

print("*"*30)
print("Solution 2")
#Solution2:
def q4_2(file_path):
    list0=file_path.split(".")
    file_extension=list0[1]
    list1=list0[0].replace("\\"," ")
    list1=list1.split(" ")
    file_name=list1[-1]
    return file_name, file_extension

file_name, file_extension = q4_2(file_path)
print(f"File Name: {file_name}")
print(f"File Extension: {file_extension}")



