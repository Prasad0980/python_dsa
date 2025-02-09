def bubble_sort(arr: list):
    if not arr:
        return -1
    if len(arr) == 1:
        return arr 
    for i in range(1,len(arr)):
        k = i
        while k >0:
            if arr[k-1] > arr[k]:
                arr[k], arr[k-1] = arr[k-1], arr[k]
            k -=1 
    return arr 

print(bubble_sort([1,2,3,4,5,6,7]))