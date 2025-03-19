def is_prime():
    num = int(input("Enter a number: "))
    if num <= 1:
        print(f"{num} is not a prime number.")
        return

    for i in range(2, int(num**0.5) + 1):  # Check divisors up to the square root of num
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")

# Run the prime checker
is_prime()
