def selection_sort(arr: list):
    for i in range(len(arr)):
        min_idx = i 
        
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j 
        
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
        
    return arr 

print(selection_sort([3,2,5,2,5,7,8,6,52,1,34,6,88,6]))