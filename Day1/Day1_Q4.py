# Given a string: 
# • If the first character is uppercase, print "Starts with uppercase" 
# • Else if the last character is lowercase, print "Ends with lowercase" 
# • Else print "Other case" 

s="Sunny"
if not s:
    print("Empty string")

first = s[:1]
last = s[-1:]
if first.isupper():
    print("Starts with uppercase")
elif last.islower():
    print("Ends with lowercase")
else:
    print("Other case")