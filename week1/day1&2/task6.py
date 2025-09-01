def removeDuplicates(arr):
    return list(set(arr))

nums = [1, 2, 3, 2, 4, 1, 5, 3]

print("Original list:", nums)
print("Without duplicates:", removeDuplicates(nums))