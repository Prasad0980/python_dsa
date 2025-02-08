from typing import List

#my solution

def findMin(nums: List[int]) -> int:
    if nums[-1]>nums[0] or len(nums)==1:
        return nums[0]
    left, right = 0, len(nums)-1 
    while left <= right:
        mid = left + (right-left)//2 
        if nums[mid] >= nums[0]:
            left = mid + 1 
        else:
            if mid == len(nums)-1 and nums[mid-1]>nums[mid]:
                return nums[mid]
            elif nums[mid-1]>nums[mid]<nums[mid+1]:
                return nums[mid]
            else:
                right = mid 


#deepseek solution

def findMin(nums: List[int]) -> int:
    if nums[-1] > nums[0] or len(nums) == 1:
        return nums[0]
    
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] >= nums[0]:
            left = mid + 1
        else:
            right = mid
    return nums[left]
print(findMin([12,13,14,15,16,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11]))

#Basically, in my solution, i have added a check to see if the element is actually the smallest.
# That is not essential becasue when we do while left<right, the loop exits when both are same.
#The loop would exit at minimum.