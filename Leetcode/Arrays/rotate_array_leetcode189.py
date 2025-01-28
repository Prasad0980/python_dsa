from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k%len(nums)
        l, h = 0, len(nums)-1
        # while h >= l:
        #     nums[l], nums[h] = nums[h], nums[l]
        #     l += 1
        #     h -= 1
        a, b, c ,d = 0, k-1, k, len(nums) -1 
        # while b >=a :
        #     nums[a], nums[b] = nums[b], nums[a]
        #     a +=1 
        #     b -=1 
        # while d >= c:
        #     nums[c], nums[d] = nums[d], nums[c]
        #     c +=1 
        #     d -=1 
        # return nums
        return self.reverse(c,d,self.reverse(a,b,self.reverse(l, h, nums)))

    def reverse(self, l, h, arr):
        while h>=l:
            arr[l], arr[h] = arr[h], arr[l]
            l+=1 
            h-=1
        return arr
        
s= Solution()
print(s.rotate([1,2,3,4,5], 1))