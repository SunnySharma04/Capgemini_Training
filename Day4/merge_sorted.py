def merge(nums1, n, nums2, m):
    i = n-1
    j = m-1
    k = n+m-1
    while j>= 0:
        if i>=0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1


nums1 = [0,1,2,3,0,0,0]
nums2 = [2,5,6]

merge(nums1, 4, nums2, 3)
print(nums1)