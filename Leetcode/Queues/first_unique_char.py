class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = dict()
        for item in s:
            if item in hash_map:
                hash_map[item] += 1
            else:
                hash_map[item] = 1 
        for item in hash_map:
            if hash_map[item] == 1:
                return s.index(item)
        return -1