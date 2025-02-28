class Student:
    num_of_students = 0


    def __init__(self, name, age):
        self.name = name
        self.age = age
        #Student.num_of_students += 1
        self.add_student()

    @classmethod
    def add_student(cls):
        cls.num_of_students += 1
        cls.test(cls.num_of_students)

    @classmethod
    def number_of_students(cls):
        return cls.num_of_students

    @staticmethod #Mặc định một hàm bất kỳ một là self or tên biến. Trong một số TH, biến ko tham chiếu đến thuộc tính của đối tượng th ta thêm @staticmethod
    def test(nth):
        print(f"Đã thêm sv thứ {nth} thành công!")



#%% Khởi tạo đối tượng
St1=Student("John", 20)

#%% Khởi tạo đối tượng
St2=Student("Danny", 14)

#%% SL đối tượng sv đa được khởi tọa
print(Student.num_of_students)
print(Student.number_of_students())