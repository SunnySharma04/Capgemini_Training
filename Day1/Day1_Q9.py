# Given a list: 
# • If the list length is even 
#         o Compare first 2 elements and last 2 elements, Slice with same element otherwise slice with different elements. 
# • Else print "Odd length list" 

nums = [1, 2, 3, 4, 1, 2]
if len(nums) % 2 != 0:
    print("Odd length list")
if len(nums) < 4:
    print("List too short")

first_two = nums[:2]
last_two = nums[-2:]

if first_two == last_two:
    print("Slices with same elements")
else:
    print("Slices are different")