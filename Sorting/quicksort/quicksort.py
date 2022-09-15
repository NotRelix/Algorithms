# Quicksort
# Worst Case: O(n^2)

def quicksort(array):
    if len(array) < 2:                  # Base Case: Arrays with 0 or 1 elements are already sorted
        return array
    else:
        pivot = array[0]                # Recursive Case
        less = []
        greater = []

        for i in array[1:]:
            if i <= pivot:              # Sub-array of all elements less than the pivot
                less.append(i)
            else:                       # Sub-array of all elements greater than the pivot
                greater.append(i)       

        return quicksort(less) + [pivot] + quicksort(greater)

# Test Cases
print(quicksort([10, 5, 2, 3]))         # [2, 3, 5, 10]
print(quicksort([7, 4, 2, 6, 9, 3]))    # [2, 3, 4, 6, 7, 9]