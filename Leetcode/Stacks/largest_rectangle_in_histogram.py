def largest_rectangle(arr):
    stack = []
    max_rec = 0
    
    for i in range(len(arr)):
        while stack and arr[stack[-1]] > arr[i]:
            height = arr[stack.pop()]
            # Calculate width based on boundaries
            if stack:  # If stack not empty
                width = i - stack[-1] - 1
            else:  # If stack is empty
                width = i
            max_rec = max(max_rec, height * width)
            print(max_rec)
        stack.append(i)
    
    # Process remaining elements in the stack
    i = len(arr)
    while stack:
        height = arr[stack.pop()]
        if stack:
            width = i - stack[-1] - 1
        else:
            width = i
        max_rec = max(max_rec, height * width)
        print(max_rec)
    
    return max_rec


print(largest_rectangle([4,2,0,3,2,5]))
        