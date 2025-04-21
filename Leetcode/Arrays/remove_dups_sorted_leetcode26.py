from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """Works in O(N) time but is but complex"""
        # for i in range(1, len(nums)):
        #     if nums[i] > nums[i-1]:
        #         continue 
        #     else:
        #         pos = i
        #         break 
        # else:
        #     return len(nums)
        # max = nums[pos]
        # for j in range(pos+1, len(nums)):
        #     if nums[j] > max:
        #         max = nums[j]
        #         nums[pos], nums[j] = nums[j], nums[pos]
        #         pos +=1 
        # return pos
        
        """A better way"""
        l = 1 
        
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l +=1 
        return l
        

S = Solution()
print(S.removeDuplicates([1,1,2,2.3]))