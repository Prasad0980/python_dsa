def linear_search(arr, target):
    """
    Perform a linear search on the list `arr` to find the `target` value.
    
    Parameters:
        arr (list): The list of elements to search through.
        target: The value to search for.
    
    Returns:
        int: The index of the target if found, otherwise -1.
    """
    for index, value in enumerate(arr):  # Iterate through the list
        if value == target:  # Compare current element with target
            return index  # Return the index if found
    return -1  # Return -1 if target is not found


# Example usage
arr = [3, 5, 2, 8, 10, 7]
target = 8

result = linear_search(arr, target)

if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found in the list.")