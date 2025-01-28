from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int: 
        nums.sort()
        diff = float('inf')
        s_f = None 
        for i in range(len(nums)-2):
            l, h = i+1, len(nums)-1
            
            while h>l:
                s = nums[i] + nums[l] + nums[h] 
                if s == target:
                    return s
                delta = abs(target - s)
                if delta < diff:
                    s_f = s
                    diff = delta
                if target > s:
                    l +=1 
                    # while h>l and nums[l] == nums[l-1]:
                    #     l +=1 
                elif target < s:
                    h -=1 
                    # while h>l and nums[h] == nums[h+1]:
                    #     h -=1 

        return s_f

        

s = Solution()
print(s.threeSumClosest([1,1,1,1,1,1,1,1,1,1], 1))