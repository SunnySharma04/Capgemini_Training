# Given a string: 
# • If it starts with "A" 
#         o If it ends with "Z" → print "Valid AZ string" 
#         o Else → print "Starts with A but invalid end" 
# • Else → print "Invalid string" 

s = "ABCDEGZ"
if s.startswith("A"):
    if s.endswith("Z"):
        print("Valid AZ string")
    else:
        print("Starts with A but invalid end")
else:
    print("Invalid string")
