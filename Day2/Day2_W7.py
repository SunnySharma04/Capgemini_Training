# W7. Count how many times a specific digit appears in a number

n = int(input("Enter a number: "))
target = int(input("Enter the digit to count: "))
count = 0

if n == 0 and target == 0:
    count = 1

while n > 0:
    digit = n % 10
    if digit == target:
        count += 1
    n //= 10

print("Count:", count)