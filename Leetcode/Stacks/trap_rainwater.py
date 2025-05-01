from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0
        
        for i, h in enumerate(height):
            while stack and height[i] > height[stack[-1]]:
                h = height[stack.pop()]
                if stack:
                    width = i - stack[-1] - 1
                else:
                    break 
                water += (min(height[i], height[stack[-1]])-h)*width 
            stack.append(i)
        return water
            
                    
s = Solution()
print(s.trap([4]))

#this can also be done with the help of two pointers.