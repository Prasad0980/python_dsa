class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) <2:
            return ""
        # for i in range(len(s)):
        #     if s[i].islower():
        #         if s[i].upper() in s:
        #             continue 
        #         else:
        #             prev = s[:i]
        #             latter = s[i+1:]
        #             t = Solution.longestNiceSubstring(self, prev)
        #             q = Solution.longestNiceSubstring(self, latter)
        #             return t if len(t) >= len(q) else q

        #     if s[i].isupper():
        #         if s[i].lower() in s:
        #             continue
        #         else:
        #             prev = s[:i]
        #             latter = s[i+1:]
        #             k = Solution.longestNiceSubstring(self, prev)
        #             l = Solution.longestNiceSubstring(self, latter)
        #             return k if len(k)>=len(l) else l
        # return s
        letters = set(s)
        for i in range(len(s)):
            if s[i].swapcase() not in letters:
                left = Solution.longestNiceSubstring(self, s[:i])
                right = Solution.longestNiceSubstring(self, s[i+1:])
                
                return left if len(left)>= len(right) else right
        return s        

s = Solution()
print(s.longestNiceSubstring("yazaAaY"))
                    
