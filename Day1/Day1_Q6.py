# Take a string: 
# • If the string length ≥ 5 
#       o Check whether the middle character is a vowel 
# • Else print "String too short"

s = "Python"
if len(s) < 5:
    print("String too short")

mid_index = len(s) // 2
mid_char = s[mid_index:mid_index + 1]

vowels = "aeiouAEIOU"
if mid_char in vowels:
    print("Middle character is a vowel")
else:
    print("Middle character is not a vowel")