def score_parenthesis(s: str):
    stack = [0]
    
    for item in s:
        if item == "(":
            stack.append(0)
        else:
            val = stack.pop()
            stack[-1] += max(2*val, 1)
    return stack[0]
            
print(score_parenthesis("((()())())"))