from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] !=9:
                digits[i]+=1
                return digits
            elif digits[i] == 9:
                digits[i] = 0
                if i != 0:
                    continue
                else:
                    digits.insert(0,1)
                    return digits
                
        #More readable solution below.
        

        # for i in range(len(digits)-1, -1, -1):
        #     if digits[i] < 9:
        #         digits[i] += 1
        #         return digits
        #     digits[i] = 0
        
        # digits.insert(0, 1)
        # return digits

s = Solution()
print(s.plusOne([4,4,4]))