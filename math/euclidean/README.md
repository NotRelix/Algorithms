# Euclidean Algorithm

> Time complexity: O(log n)

### Description:
This algorithm is one way in finding the *greatest common factor* (GCF) of two positive integers

![image](https://user-images.githubusercontent.com/111989096/191981570-16a33724-b809-4ff2-8d55-2fda76e31285.png)

### Explanation:
1. Find the remainder of the 2 numbers
2. The x value will be replaced with the old y value
3. The y value will be replaced with the remainder
4. Repeat the process until you end up with remainder 0
5. The GCF is the value of y
