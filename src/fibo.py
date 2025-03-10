#
# Fibonarchi
#
#
#   written by chatgpt
#

def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Print first 10 Fibonacci numbers
for i in range(1, 11):
    print(fibonacci(i), end=" ")
