from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = list()
        cache = dict()
        for item in nums2:
            while stack and stack[-1]<item:
                cache[stack.pop()] = item 
            stack.append(item)
            
        while stack:
            cache[stack.pop()] = -1 
        return [cache[item] for item in nums1]
    
s = Solution()
print(s.nextGreaterElement([4,1,2], [1,3,4,2]))