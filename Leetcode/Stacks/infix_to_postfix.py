def infix_to_postfix(expr: str):
    
    stack = list()
    output = list()
    
    if isinstance(expr, str):
        tokens = expr.split()
        print(tokens)
    else:
        raise Exception("Not a string")
    
    precedence = {"+" : 1, "-": 1, "*": 2, "/": 2, "^": 3, "(": 0}
    
    for token in tokens:
        if token not in precedence and token not in "()":
            output.append(token)
        
        elif token == "(":
            stack.append(token)
        
        elif token == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                raise ValueError("Missing Parentheses")
        else:
            if not stack:
                stack.append(token)
            else:
                if precedence.get(stack[-1]) < precedence.get(token):
                    stack.append(token)
                else:
                    if token =="^":
                        stack.append(token)
                    else:
                        while stack and precedence.get(stack[-1]) >= precedence.get(token):
                            output.append(stack.pop())
                        stack.append(token)
    while stack:
        output.append(stack.pop())
    return " ".join(output)

print(infix_to_postfix("1 + 2 / 3 * 4 - 5"))