#%% Superclass (Lớp cha)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

#%% Subclass (Lớp con) kế thừa từ Person
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age) #Gọi structor của lớp cha
        self.student_id = student_id

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old, and my ID is {self.student_id}.")

#%% Tạo đối tượng từ lớp con
student = Student("John", 18, "S789")
student.introduce()
