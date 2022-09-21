# Euclidean Algorithm
# Worst Case: O(log n) 

def euclidean(x, y):
    if x < y: x, y = y, x               # Swaps x and y if x is smaller than y to avoid remainder errors

    remainder = x % y

    while remainder != 0:               # Base Case
        x = y
        y = remainder
        remainder = x % y

    return y

# Test Cases:
print(euclidean(10, 5))                 # 5
print(euclidean(12, 8))                 # 4
