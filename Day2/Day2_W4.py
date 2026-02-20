# W4. Count how many even and odd digits are present in a number

n = int(input("Enter a number: "))
even_count = 0
odd_count = 0

if n == 0:
    even_count = 1

while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    n //= 10

print("Even digits:", even_count)
print("Odd digits:", odd_count)