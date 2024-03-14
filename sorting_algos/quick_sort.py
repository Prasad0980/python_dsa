def quicksort(arr: list):
    if len(arr) < 2:
        return arr
    x = arr[-1]
    l = [item for item in arr if item > x]
    e = [item for item in arr if item == x]
    s = [item for item in arr if item < x]

    l = quicksort(l)
    s = quicksort(s)
    return s + e + l


print(quicksort([8,7,6,5,4,3,2,1])) 