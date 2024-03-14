def inplace_quick_sort(arr, a, b):
    if a >= b:
        return arr
    pivot = arr[b]
    l = a 
    r = b-1 
    while l <= r:
        while l <= r and arr[l] < pivot:
            l +=1 
        while l <= r and pivot < arr[r]:
            r -= 1
        if l<=r:
            arr[l], arr[r] = arr[r], arr[l]
            l , r = l + 1, r - 1

    arr[l], arr[b] = arr[b], arr[l]
    print(arr)
    inplace_quick_sort(arr, a, l-1)
    inplace_quick_sort(arr, l+1, b)
    return arr

print(inplace_quick_sort([2,1,6,5,4,9,12,8], 0, 7))
