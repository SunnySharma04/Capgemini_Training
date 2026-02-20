# Given a string, check whether the last character is a digit using slicing, if digit-> Ends with digit otherwise Ends with character / Ends with special symbol.

s = "Hello123!"
if not s:
    print("Empty string")
last = s[-1:]
if last.isdigit():
    print("Ends with digit")
elif last.isalpha():
    print("Ends with character")
else:
    print("Ends with special symbol")