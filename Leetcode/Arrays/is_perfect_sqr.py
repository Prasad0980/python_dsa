#Illustration of binary search method.
# This problem could have been solved by iterating in a iterable and checking for perfect square. But then it will run in O(N) time.
# When we solve by binary search method, the problem is solved with O(logn) time.

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True 
        left, right = 1, num//2 
        while left <= right:
            mid = left + (right-left)//2 

            if mid**2 == num:
                return True 
            elif mid **2 > num:
                right = mid - 1 
            else:
                left = mid + 1
        return False 