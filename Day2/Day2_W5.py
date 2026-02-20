# W5. Check whether a number is a palindrome using while loop

n = int(input("Enter a number: "))
original = n
rev = 0

while n > 0:
    rev = rev * 10 + (n % 10)
    n //= 10

if rev == original:
    print("Palindrome number")
else:
    print("Not a palindrome")