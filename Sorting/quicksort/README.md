# Quicksort Algorithm
**Time Complexity (Worst Case): O(n^2)**

**Quicksort Algorithm** - takes an unsorted array which then takes a single element in the array (the pivot), for instance the first element, there will then be 2 arrays, one for the left (less than the pivot), and one for the right (greater than the pivot). Once that's done, it will recurse that list by setting the pivot as the first element, and the cycle repeats.

#### How to pick a pivot point?
  - *(My Personal preferrence)* Always pick the first element 
  - Always pick the last element
  - Pick a random element
  - Pick the median

### Here's my simple illustration of Quicksort with recursion:
![quicksort_illustration](https://user-images.githubusercontent.com/111989096/190842191-6cfaa570-7dcc-44b1-b4d5-887da35c9179.png)
### Explanation:
  1. Takes 10 as the *pivot*, then partitions the given array around the pivot
  2. Continues doing so until it reaches the **Base Case** (if the array has less than 2 elements)
  3. Returns and combines the values from each recursion with the *sorted array* + pivot + *the other sorted array*
  4. End up with a **Sorted Array**