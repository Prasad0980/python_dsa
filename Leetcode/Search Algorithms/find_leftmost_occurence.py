def find_left_most_occurence(nums, target):
    left, right = 0, len(nums)-1 
    found = -1
    while left<= right:
        mid = left + (right-left)//2

        
        if nums[mid]== target:
            found = mid
            right = mid - 1 
        elif nums[mid] > target: 
            right = mid - 1 
        else:
            left = mid + 1 
    return found 
            
print(find_left_most_occurence([0,1,1,1,2,2,5,6,9,9,10], 10))