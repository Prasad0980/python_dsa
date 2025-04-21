from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = -1
        count = 0

        for item in nums:
            if count == 0:
                a = item 

            if a == item:
                count +=1 
            else:
                count -=1 

        return a 
sol = Solution()
a = sol.majorityElement([3,2,3,2,2])
print(a)