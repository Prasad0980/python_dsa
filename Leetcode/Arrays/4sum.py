from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) <4:
            return []
        nums.sort()
        res = list()
        i = 0
        while i < len(nums)-3:
            j = i+1
            while j < len(nums)-2:
                k, l = j+1, len(nums) - 1
                while l > k:
                    s = nums[i] + nums[j] + nums[k] + nums[l]
                    if s == target:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        while k<l and nums[k]==nums[k+1]:
                            k+=1
                        while k<l and nums[l] == nums[l-1]:
                            l-=1
                        l -= 1
                        k += 1
                    elif s < target:
                        k += 1
                    else:
                        l -= 1
                while j < len(nums)-2 and nums[j] == nums[j+1]:
                    j +=1 
                j += 1
            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                i +=1 
            i += 1
        return res


s = Solution()
print(s.fourSum([2,2,2,2,2,2,2,2,2], 8))
