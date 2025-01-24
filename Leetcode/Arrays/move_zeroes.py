from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 1
        """Brute force solution"""
        """This was my thought process in the first go. It takes O(N^2) time to run"""
        # flag = True
        # for i in range(len(nums)-1, -1, -1):
        #     if nums[i] == 0 and flag:
        #         continue
        #     elif nums[i] !=0 and flag:
        #         flag = False
        #     elif nums[i] == 0:
        #         for j in range(i, len(nums)-1):
        #             if nums[j+1] == 0:
        #                 break
        #             nums[j], nums[j+1] = nums[j+1], nums[j]
        #     else:
        #         continue
        # return nums

        # 2
        """A better way."""
        """I came up with second soltion. In this I created two pointers and 
        changed the slower one only when it was not equal to 0. Kind of close to ideal
        solution but it has got some redundant conditions and higher space complexity.
        Takes O(N) time but has high space complexity."""

        # i, j = 0, 1
        # while j <= len(nums) -1:
        #     if nums[i] == 0 and nums[j] != 0:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         i +=1
        #     elif (nums[i] != 0 and nums[j] != 0) or (nums[i] !=0 and nums[j] == 0):
        #         i +=1
        #     j+=1
        # return nums

        # 3
        """The ideal one.
        Takes O(N) time. Sace complexity is low. """
        pos = 0

        # First pass: place all non-zero elements
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1


s = Solution()
print(s.moveZeroes([0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))


"""Learnings:
1. Two pointer approach introduction.
2. How two pointers can be used.
3. Swapping in place as we did in last solution takes less space. """
