def is_palindrome():
    text = input("Enter a string: ").lower()  # Convert to lowercase for case-insensitivity
    if text == text[::-1]:  # Compare the string with its reverse
        print("It's a palindrome!")
    else:
        print("It's not a palindrome.")

# Run the palindrome checker
is_palindrome()
