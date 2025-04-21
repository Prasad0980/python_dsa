from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ini_sum = sum(nums[:k])
        max_sum = ini_sum
        for i in range(len(nums)-k):
            ini_sum = ini_sum + nums[i+k] - nums[i]
            if ini_sum> max_sum:
                max_sum = ini_sum 
        return max_sum/k 
s= Solution()
print(s.findMaxAverage([0,4,0,3,2],1))