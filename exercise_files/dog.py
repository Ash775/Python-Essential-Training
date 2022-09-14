class Dog:
    def __init__(self, name):
        self.name = name
        self.legs = 4

    def speak(self):
        print(self.name + " Barks!")

class Cat():
    def __init__(self, name):
        self.name = name
        self.legs = 4

    def speak(self):
        print(self.name + " says Meow!")

my_Dog = Dog("Franky")
my_Dog.speak()
print(my_Dog)

another_Dog = Dog("Dooby")
another_Dog.speak()
print(another_Dog)

my_Cat = Cat("Cindy")
my_Cat.speak()
print(my_Cat)

my_Cat2 = Cat("Jennyfer")
my_Cat2.speak()
print(my_Cat2)