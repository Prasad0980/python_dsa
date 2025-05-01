
def calculate(s: str) -> int:
    num = 0
    operator = "+"
    stack = list()

    for token in s:
        if token == " ":
            continue 
        elif token.isdigit():
            num = num*10 + int(token)
        else:
            if operator == "+":
                stack.append(num)
            if operator == "-":
                stack.append(-num)
            if operator == "/":
                val = stack.pop()
                stack.append(val//num if val>=0 else -(-1*val//num))
            if operator =="*":
                val = stack.pop()
                stack.append(val*num)
            operator = token      
            num = 0          
    
    if operator == "+":
        stack.append(num)
    if operator == "-":
        stack.append(-num)
    if operator == "/":
        val = stack.pop()
        stack.append(val//num)
    if operator =="*":
        val = stack.pop()
        stack.append(val*num)
        

    return sum(stack)

print(calculate("6+4-5    /6*7  + 8  "))
