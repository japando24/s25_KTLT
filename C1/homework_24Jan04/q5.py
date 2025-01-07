#Q5: Viết hàm xử lý kiểm tra địa chỉ email hợp lệ, nếu email hợp lệ thì trả về user_name và domain_name.
#Vd: với email: iloveuel@uel.edu.vn à username: iloveuel, domain_name: uel.edu.vn

#str="iloveuel@uel.edu.vn"
def q5():
    str=input("Enter your email: ")
    str.strip()
    list=str.split("@")
    user_name=list[0]
    domain_name=list[1]
    print(f"Email: {str}")
    print(f"User name: {user_name}")
    print(f"Domain name: {domain_name}")

while True:
    q5()