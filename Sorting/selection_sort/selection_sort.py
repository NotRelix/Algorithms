# Selection Sort
# Worst Case O(n^2)

# Checks for the smallest value in the array
def findSmallest(arr):
    smallest = arr[0]               # Stores the smallest value
    smallest_index = 0              # Stores the index of the smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index

# Sorts the array from smallest to biggest
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)            # Finds the smallest value
        newArr.append(arr.pop(smallest))        # Then adds it to the new array

    return newArr
    
# Test Cases
print(selectionSort([5, 3, 6, 2, 10]))          # [2, 3, 5, 6, 10]
print(selectionSort([9, 1, 3, 12, 8]))          # [1, 3, 8, 9, 12]