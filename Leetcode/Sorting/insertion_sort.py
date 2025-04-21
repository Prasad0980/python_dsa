def insertion_sort(arr: list):
    if not arr:
        return -1
    if len(arr) == 1:
        return arr
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be inserted
        j = i - 1
        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Insert the key in its correct position
    return arr

print(insertion_sort([1,3,2,4,5,2]))