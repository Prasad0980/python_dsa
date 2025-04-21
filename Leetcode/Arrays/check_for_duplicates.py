from typing import List
"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3."""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """Sol 1. Runs in O(N) time but dict is not really needed here. A better solution is below. Better in memory consumption"""
        # cache = dict()
        # for i in range(len(nums)):
        #     if cache.get(nums[i]) is not None:
        #         return True 
        #     else:
        #         cache[nums[i]] = i
        # return False 
        """Sol 2: Uses set"""
        cache = set()
        for item in nums:
            if item in cache:
                return True
            else:
                cache.add(item)
        return False

        """Sol 3: uses conversion of list to set. Runs in O(N) time"""
        # return len(set(nums)) < len(nums)

