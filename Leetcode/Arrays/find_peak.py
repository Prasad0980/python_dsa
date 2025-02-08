from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1 or nums[0] > nums[1]: #Here i learnt one imp thing. We should not have nums[0] > nums[1] before len(nums)==1
            return 0                          # Because if in case there's an array of length 1, it will throw error.  
        if nums[-1]> nums[-2]:
            return len(nums)-1 
        left, right = 0, len(nums)-1 
        while left <= right:
            mid = left + (right-left)//2 
            if nums[mid-1]<nums[mid]>nums[mid+1]:
                return mid 
            if nums[mid+1] > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1 
                
s= Solution()
print(s.findPeakElement([1,2,3,1]))