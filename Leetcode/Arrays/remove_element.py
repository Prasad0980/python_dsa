from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j], nums[i] = nums[i], nums[j]
                j+=1
        return j
            



s = Solution()
a = s.removeElement([0,1,2,2,3,0,4,2], 2)
print(a)

        