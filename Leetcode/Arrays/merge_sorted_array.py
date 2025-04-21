from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # if n!=0 and m!=0:
        if n != 0 and m != 0:
            k = m+n-1
            o = m-1
            d = n - 1
            count = 0
            while k >= 0 and count != n:
                if o != -1 and nums1[o] > nums2[d]:
                    nums1[k], nums1[o] = nums1[o], nums1[k]
                    o -= 1
                else:
                    nums1[k] = nums2[d]
                    count += 1
                    d -= 1
                k -= 1
        elif m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        return nums1


sol = Solution()
a = sol.merge([0, 0, 3, 0, 0, 0, 0, 0, 0], 3, [-1, 1, 1, 1, 2, 3], 6)
print(a)


# more correct solution
"""  i = m -1
      j = n -1
      k = m + n -1
      while i >= 0 and j >= 0:
          if nums1[i] >nums2[j]:
              nums1[k]=nums1[i]
              i-=1
          else:
              nums1[k]=nums2[j]
              j-=1
          k-=1
      ##if there are remaining element in nums2
      while j>=0:
          nums1[k]=nums2[j]
          j-=1
          k-=1"""
