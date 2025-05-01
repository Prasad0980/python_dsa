def evaluate_postfix(expr: str):
    tokens = expr.strip().split()
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    stack = list()
    
    for token in tokens:
        if token in "+-^*/":
            if len(stack) < 2:
                raise ValueError("Not sufficient operands")
            else:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a+b)
                elif token == "-":
                    stack.append(a-b)
                elif token == "^":
                    stack.append(a**b)
                elif token == "*":
                    stack.append(a*b)
                else:
                    stack.append(a/b)
        else:
            stack.append(float(token))
    return stack[0]

print(evaluate_postfix("1 2 3 / 4 * + 5 -"))
        
    
    