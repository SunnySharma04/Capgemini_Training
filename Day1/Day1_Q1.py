# Given a list of numbers, print "Valid slice" only if the first two elements are equal to the last two elements.

nums = [1, 2, 3, 4, 1, 2]
if len(nums) < 4:
        print("List too short")
if nums[:2] == nums[-2:]:
    print("Valid slice")
else:
    print("Invalid slice")