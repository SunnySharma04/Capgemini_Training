# Write a program that checks whether a string is a palindrome using slicing. 

s = "abcdcba"
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")