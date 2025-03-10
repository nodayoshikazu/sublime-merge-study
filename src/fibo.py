#
# Fibonarchi
#
#
#   written by chatgpt
#
class Fibb:
    def fibonacci(self, n):
        if n <= 0:
            return "Invalid input"
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def test(self, max):
        # Print first 10 Fibonacci numbers
        for i in range(1, max):
            print(self.fibonacci(i), end=" ")

f = Fibb()
f.test(30)
