def maximal_rectangle(arr: list):
    area = 0
    stack = list()

    for i in range(len(arr[0])):
        prev = 0
        for item in arr:
            if int(item[i]) != 0:
                item[i] =  int(item[i]) + prev 
            else:
                item[i] = int(item[i])
            prev = int(item[i])
    # print(arr)
    for heights in arr:
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                if stack:
                    width = i - stack[-1] -1 
                else:
                    width = i 
                area = max(area, height*width)
            stack.append(i)
        i = len(heights)   
        while stack:
            height = heights[stack.pop()]
            if stack:
                width = i - stack[-1] -1 
            else:
                width = i 
            area = max(area, height*width)
        # print(area)
    return area 

print(maximal_rectangle([["1"]]))


