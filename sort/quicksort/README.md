# Quicksort Algorithm

> Time Complexity: O(n^2)

### Description:
takes an unsorted array which then takes a single element in the array (the pivot), for instance the first element, there will then be 2 arrays, one for the left (less than the pivot), and one for the right (greater than the pivot). Once that's done, it will recurse through that new list by setting the pivot as the first element, and the cycle repeats.

### How to pick a pivot point?
  - Always pick the first element 
  - Always pick the last element
  - Pick a random element
  - Pick the median

---

![Quicksort](https://user-images.githubusercontent.com/111989096/191301859-bc1a4378-4d04-4b2d-b48b-d5fbf1378c3d.png)
### Explanation:
  1. Takes 10 as the *pivot*, then partitions the given array around the pivot
  2. Continues doing so until it reaches the **Base Case** (if the array has less than 2 elements)
  3. Returns and combines the values from each recursion with the *sorted array* + pivot + *the other sorted array*
  4. End up with a **Sorted Array**
