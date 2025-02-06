from typing import List
def searchInsert( nums: List[int], target: int) -> int:
    left, right = 0, len(nums)-1 
    
    while left <= right:
        mid = left + (right-left)//2 
        
        if nums[mid] == target:
            return mid 
        elif nums[mid] > target:
            right = mid - 1 
        else:
            left = mid + 1 
    return left 

print(searchInsert([1,3,5,6], 7))
    