from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
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
        #i, j = 0, 1
        # while j <= len(nums) -1:
        #     if nums[i] == 0 and nums[j] != 0:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         i +=1
        #         j +=1 
        #     elif nums[i] == 0 and nums[j] == 0:
        #         j += 1
        #     else:
        #         i +=1 
        #         j+= 1


        # while j <= len(nums) -1:
        #     if nums[i] == 0 and nums[j] != 0:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         i +=1
        #     elif (nums[i] != 0 and nums[j] != 0) or (nums[i] !=0 and nums[j] == 0):
        #         i +=1 
        #     j+=1 
        # return nums
        pos = 0
        
        # First pass: place all non-zero elements
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1


            
                
            





s = Solution()
print(s.moveZeroes([1,0,1]))