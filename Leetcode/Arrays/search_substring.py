
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                j = i
                for _ in range(len(needle)):
                    if haystack[j] == needle[_]:
                        j += 1
                    else:
                        break
                else:
                    return i 
        return -1

s = Solution()
print(s.strStr("kabc", "bc"))
        