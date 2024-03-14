#Selection sort runs in O(N^2) times in both its best and worst case
# Selection sort it neither adaptive not stable

def selection_sort(arr):
    for i in range(len(arr)-1):
        j = i+1
        small = i
        temp = arr[i]
        while j < len(arr):
            if temp > arr[j]:
                temp = arr[j]
                small = j
            j += 1

        arr[small], arr[i] = arr[i], temp
    return arr

def selection_sort_2(arr):
    for i in range(len(arr)-1):
        small = i
        temp = arr[i]
        for j in range(i+1, len(arr)):
            if temp > arr[j]:
                temp = arr[j]
                small = j 
        arr[small], arr[i] = arr[i], temp
    return arr


print(selection_sort_2([7,1,3,2,8,4,5,3,6]))
print(selection_sort([7,1,3,2,8,4,5,3,6]))