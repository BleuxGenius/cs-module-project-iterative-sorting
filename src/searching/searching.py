# For a binary search, the array A must be sorted. The main idea of a binary search is to divide the given sorted array A into two subarrays at each step and look for the key element k in one of the two subarrays. This idea improves the time complexity from O(n) (Linear search) to O(logn).



def linear_search(arr, target):
    # Your code here
    for i in arr:
        if i == target:
            return arr.index(i)


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
# find the midpoint 
    # Your code here
    left = 0
    right = len(arr) -1

    while left <= right:
        mid = (left + right) // 2 

        if arr[mid] == target:
            return mid

        # check to see on the right or left side of target
        if arr[mid] < target:
            arr = arr[:mid]
            # update the left index
            # we can leave behind the midpoint, it didn't match 
            left = mid + 1 

        else: # if array is greater than target
            arr = arr[mid:]
            right = mid - 1
        # if element dosent exist
    return -1  # not found
