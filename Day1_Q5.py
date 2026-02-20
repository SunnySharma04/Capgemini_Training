# Given a list of integers: 
# • If the sum of first half > sum of second half, print "First half greater" 
# • Else if equal, print "Equal halves" 
# • Else print "Second half greater"

nums = [1, 2, 3, 4, 5, 6, 7]
if not nums:
    print("Empty list")

mid = len(nums) // 2
first_half = nums[:mid]
second_half = nums[mid:]

sum_first = sum(first_half)
sum_second = sum(second_half)

if sum_first > sum_second:
    print("First half greater")
elif sum_first == sum_second:
    print("Equal halves")
else:
    print("Second half greater")