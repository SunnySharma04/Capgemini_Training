str = "Amazing scenarios all over india"
vowels = "aeiouAEIOU"
lst = [word for word in str.split() if word[0] in vowels]
print(lst)