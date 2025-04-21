"""Description:

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type."""

class Solution:
    def isValid(self, s: str) -> bool:
        # if len(s)%2 != 0:
        #     return False
        if len(s) == 1:
            return False
        stack = list()
        brackets = {")": "(", "}": "{", "]": "["}
        for item in s:
            if item in "({[":
                stack.append(item)
            
            elif stack and stack.pop() == brackets.get(item):
                    continue 
            else:
                return False 
        return True if not stack else False  

        