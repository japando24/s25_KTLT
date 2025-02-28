#Định nghĩa lớp Student
class Student:
    def __init__(self, s_name, s_age,s_student_id):
        self.name = s_name
        self.age = s_age
        self.student_id = s_student_id

    def introduce(self):
        #Phương thức hiển thị thông tin sv
        print(f"My name is {self.name}, and my age is {self.age} years old, ID: {self.student_id}")

    def __repr__(self):
        return f"Student({self.name}, {self.age}, {self.student_id})"

#%% Tạo đối tượng từ lớp Student
st1=Student("Alice",20,"K123")
st2=Student("Bob",22,"K456")

#%% Gọi thuộc tính, phương thức của đối tượng sv
print(st1.name) #Truy xuất thuộc tính tên của đôi tượng St1
st1.introduce() #Truy xuâất phương thức introduce() của đối tượng St1
st2.introduce()

#%% In thông tin (cách khác)
print(st1.__dict__)
print(st1) #Bắt buộc def __repr__ (self)