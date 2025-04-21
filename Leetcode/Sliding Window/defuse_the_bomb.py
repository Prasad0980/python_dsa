from typing import List
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0]*len(code)
        ret = list()
        if k > 0:
            right = k 
            window_sum = sum(code[1:right+1])
            for i in range(len(code)):
                if i ==0:
                    ret.append(window_sum)
                else:
                    right  = right +1 if right != len(code) -1 else 0
                    window_sum = window_sum - code[i] + code[right]
                    ret.append(window_sum)
        if k < 0:
            ind = len(code) - (-1)*k
            window_sum = sum(code[ind:])
            for i in range(len(code)):
                if i ==0:
                    ret.append(window_sum) 
                else:
                    window_sum = window_sum - code[ind] + code[i-1]
                    ret.append(window_sum)
                    ind = ind + 1 if ind !=len(code)-1 else 0
        return ret 
    

s= Solution()
print(s.decrypt([2,4,9,3], -2)) #[5.7.9.6.3]