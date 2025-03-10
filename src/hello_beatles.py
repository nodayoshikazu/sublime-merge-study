#
#  hello_beatles.py
#
#
#   written by chatgpt
#

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def tease(self):
        print(f"Don't you come close")

    def mytwobits(self):
        print(f"my name is {self.name} {self.age}")


# Create instances of Person
p1 = Person("Alice", 25)
p2 = Person("Bob", 30)
p3 = Person("Jim", 50)

# Call the greet method
p1.greet()
p2.greet()
p3.tease()
