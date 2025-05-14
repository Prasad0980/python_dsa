def longest_valid_parenthesis(s: str):
    if not s:
        return 0
    stack = list()
    len_ = 0
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(i)
        else:
            if stack:
                val = stack.pop()
                len_ = max(len_, i-val+1)
            else:
                continue
        


    return len_


print(longest_valid_parenthesis(")()()("))
