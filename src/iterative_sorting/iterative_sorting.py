#On each loop iteration, insertion sort removes one element from the array. It then finds the location where that element belongs within another sorted array and inserts it there. It repeats this process until no input elements remain.


# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
      # range returns a `range` 
    # does the range object utilize a constant amount of space?
    # range takes up a constant amount of space 
    for i in range(0, len(arr) - 1): 
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for x in range(i+1, len(arr)):
            if arr[x] < arr[smallest_index]:
                smallest_index = x


        # TO-DO: swap
        # Your code here
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


# TO-DO:  implement the Bubble Sort function below

#This simple sorting algorithm iterates over a list, comparing elements in pairs and swapping them until the larger elements "bubble up" to the end of the list, and the smaller elements stay at the "bottom".

# We begin by comparing the first two elements of the list. If the first element is larger than the second element, we swap them. If they are already in order we leave them as is. We then move to the next pair of elements, compare their values and swap as necessary. This process continues to the last pair of items in the list.

def bubble_sort(arr):
    # Your code here
    swaps = 1 
    while swaps > 0: 
        swaps = False
        # swaps = 0
    for i in range(0, len(arr) -1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            swaps = True
            # swaps += 1

    return arr

    # How would we know that we're done sorting? If items are in order then we would not have to swap any. Whenever we swap values we set a flag to True to repeat sorting process. If no swaps occurred, the flag would remain False and the algorithm will stop.

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(bubble_sort(arr1))

# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr
