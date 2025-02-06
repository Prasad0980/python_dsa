def binary_search_recursive(nums: list, target, left, right):
    if left > right:
        return -1 
    mid = left + (right-left)//2
    if nums[mid] == target:
        return mid 
    elif nums[mid] > target:
        right = mid - 1 
        return binary_search_recursive(nums, target, left, right)
    else:
        left = mid + 1
        return binary_search_recursive(nums, target, left, right)
        
print(binary_search_recursive([1,2,3,4,5,6], 4, 0, 5))