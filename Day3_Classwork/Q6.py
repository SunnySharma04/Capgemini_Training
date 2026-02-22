dict = {"Sunny":97, "Ankit":57, "Manish":75}
new_dict = {i:dict[i] for i in dict if dict[i]>=60}
print(new_dict)
# for i in dict:
#     print(i,dict[i])