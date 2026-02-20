# W2. Reverse a number using while loop and check if reversed number is greater than original

n = int(input("Enter a number: "))
original = n
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

print("Reversed:", rev)

if rev > original:
    print("Reversed number is greater than original.")
else:
    print("Reversed number is NOT greater than original.")