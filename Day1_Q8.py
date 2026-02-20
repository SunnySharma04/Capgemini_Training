# Given a string: 
# • If the first 2 characters are digits 
#         o Check whether the last 2 characters are alphabets 
# • Else print "Invalid format"

s = "21B2C3DA"
if len(s) < 4:
    print("Invalid format")

first_two = s[:2]
last_two = s[-2:]

if first_two.isdigit():
    if last_two.isalpha():
        print("Valid format")
    else:
        print("Invalid format")
else:
    print("Invalid format")