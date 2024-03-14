def merge(arr1, arr2, arr):
    i = j = 0
    while i + j < len(arr):
        if j == len(arr2) or (i < len(arr1) and arr1[i] < arr2[j]):
            arr[i+j] = arr1[i]
            i += 1
        else:
            arr[i + j] = arr2[j]
            j += 1
    return arr

def merge_sort(arr):
    n = len(arr)
    if n < 2:
        return 
    mid = n//2 
    arr1, arr2 = arr[:mid], arr[mid:n]
    merge_sort(arr1)
    merge_sort(arr2)

    merge(arr1, arr2, arr)
    return arr

a = [4, 1]
# b = [9, 6, 7, 8, 10]
# c = [0]*10 
print(merge_sort(a))