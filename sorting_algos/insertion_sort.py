#insertion sort takes O(n^2) in worst case and O(n) in the best case
#Worst case will be the case when the array is reversed or completely unsorted.
#Best case will be when the input array is fully sorted
#Insert sort is both adaptive and stable

def insertion_sort(arr):
    for k in range(1, len(arr)):
        curr = arr[k]
        j = k 
        while j>0 and arr[j-1] > curr:
            arr[j] = arr[j-1]
            j -=1
            arr[j] = curr
    return arr 

array = [5,4,3,2,1]
print(array)
print(insertion_sort(array))