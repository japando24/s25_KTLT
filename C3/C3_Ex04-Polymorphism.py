#%% Định nghĩa ớp Animal
class Animal:
    def speak(self): #Phương thức trừu tượng
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"

#%% Sử dụng đa hình
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())
