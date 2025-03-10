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

# Create instances of Person
p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

# Call the greet method
p1.greet()
p2.greet()
