def binary_search(nums: list, target):
    left, right = 0, len(nums)-1 
    while left<=right:
        mid = left + (right - left)//2 
        if nums[mid] == target:
            return mid 
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1 

print(binary_search([1,2,3,4,5,6,7,8,9,10], 5))