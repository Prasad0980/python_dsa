def bubble_sort(arr):
    for i in range(len(arr)-1):
        j = i +1 
        count = 0
        for k in range(len(arr)- j):
            if arr[k] > arr[k+1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]
                count +=1 
        if count == 0:
            break
    return arr

print(bubble_sort([9,21,4,5,2,46,23,87,54,456,2,4,34]))