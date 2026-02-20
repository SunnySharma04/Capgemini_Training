# W3. Repeatedly sum digits until a single digit is obtained

n = int(input("Enter a number: "))

while n >= 10:
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    n = s

print("Single digit:", n)