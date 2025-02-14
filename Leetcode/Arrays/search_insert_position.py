from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            if target <= nums[i]:
                return i
            elif target == nums[j]:
                return j
            elif target > nums[j]:
                return j+1
            else:
                i += 1
                j -= 1
        return i 

s = Solution()
a = s.searchInsert([1,2,3,4,5,6,8],7 )
print(a)
