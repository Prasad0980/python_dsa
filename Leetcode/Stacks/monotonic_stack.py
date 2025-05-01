def monotonic_increasing_stack(arr):
    stack = []
    for num in arr:
        # Pop elements from the stack as long as they are greater than the current number
        while stack and stack[-1] > num:
            stack.pop()
        # Push the current number to the stack
        stack.append(num)
    return stack

print(monotonic_increasing_stack([1, 2, 3, 0, 6]))