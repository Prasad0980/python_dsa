from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] = digits[i] + 1
                return digits
            else:
                digits[i] = 0
        return [1] + digits


a = Solution()
b = a.plusOne([9, 9, 0])
print(b)