from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        d_area = min(height[l], height[r])*(r-l)
        while r > l:
            if height[l] < height[r]:
                l +=1 
            elif height[l] > height[r]:
                r -=1 
            else:
                l +=1 
                r -=1 

            if min(height[l], height[r])*(r-l) > d_area:
                d_area = min(height[l], height[r])*(r-l)
        return d_area

s = Solution()
print(s.maxArea([10,1000,15,23,2,3,1,1,76,900,12]))