from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """Double pass solution"""
        # pos = 0 
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         nums[pos], nums[i] = nums[i], nums[pos]
        #         pos +=1 
        # pos = -1 
        # for i in range(len(nums)-1, -1, -1):
        #     if nums[i] == 2:
        #         nums[pos], nums[i] = nums[i], nums[pos]
        #         pos -=1 
        # return nums 
        
        """single pass solution"""

        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
            print(nums)
        return nums
    
# A very essential concept to learn here is then when we find 2, we dont increment mid variable like we do it when we find 0
# One would wonder why? This is because when we swap elements when we find 2, we do not know that the swapped element is again 2 or anything else
# Lets say the swapped element is 2, what it means is that we still need to swap that 2 again if it is not in correct place. So we dont move mid and keep it there it self.
# On the contrary, when we find 0, we increment mid. This is because, our pointer is not at the location from where we swapped. 
# Rather our pointer is at the postion where 0 is supposed to be. We know the 0 is in correct place and since our pointer (mid) is not at location from where other element came, we dont enocunter the question of what the value of swapped element is .
# This is a bit tenacious logic but if we think carefully we realise it makes sense. 
    
s = Solution()
print(s.sortColors([0,0,2,1,1,2]))