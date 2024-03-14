def sort_quick_inplace(arr, a, b):
    if a >=b:
        return arr
    mid = len(arr)//2
    if arr[b] <= arr[mid] <= arr[a]:
        arr[a], arr[b] = arr[b], arr[a]
    if arr[mid] <= arr[a] <= arr[b]:
        arr[mid], arr[a] = arr[a], arr[mid]
    if arr[b] <= arr[a]<=arr[mid]:
        arr[a], arr[b], arr[mid] = arr[b], arr[mid], arr[a]
    if arr[mid] <= arr[b] <= arr[a]:
        arr[a], arr[b], arr[mid] = arr[mid], arr[a], arr[b]
    if arr[a] <= arr[b] <= arr[mid]:
        arr[mid], arr[b] = arr[b], arr[mid]
    arr[b-1], arr[mid] = arr[mid], arr[b-1]
    pivot = arr[b-1]
    l = a+1
    r = b-2 
    while l <= r:
        while l <= r and arr[l] < pivot:
            l +=1 
        while l <= r and pivot < arr[r]:
            r -= 1
        if l<=r:
            arr[l], arr[r] = arr[r], arr[l]
            l , r = l + 1, r - 1

    arr[l], arr[b-1] = arr[b-1], arr[l]
    print(arr)
    sort_quick_inplace(arr, a, l-1)
    sort_quick_inplace(arr, l+1, b)
    return arr


print(sort_quick_inplace([2,1,6,5,4,9,12,8], 0, 7))
# a = 8; b = 6; mid = 4
# print(a, mid, b)
# a , b, mid = mid, a, b 
# print(a, mid , b)