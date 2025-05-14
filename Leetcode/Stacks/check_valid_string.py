def check_valid_string(s: str):
    stack = list()
    star = list()
    for item in s:
        if item in "*(":
            stack.append(item)
        elif not stack:
            return False
        else:
            while stack and stack[-1] != "(":
                star.append(stack.pop())
            if not stack:
                star.pop()
            else:
                stack.pop()
            while star:
                stack.append(star.pop())
    while stack:
        value = stack.pop()
        if value == "(" and not star:
            return False
        elif value == "*":
            star.append(value)
        else:
            star.pop()
    return True


print(check_valid_string("(*))"))
