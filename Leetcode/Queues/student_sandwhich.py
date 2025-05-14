class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cache = {}
        for item in students:
            if item in cache:
                cache[item] +=1 
            else:
                cache[item] = 1 
        for item in sandwiches:
            if item in cache and cache[item] != 0:
                cache[item] -=1 
            else: 
                break 
        return sum(cache.values())