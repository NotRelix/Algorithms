# Dijkstra's Algorithm

> Time Complexity: O(V^2)

### Description:
Similar to *breadth first search*, this algorithm finds the shortest path from start to finish, but one difference is that this algorithms uses the weight of the edges to find the shortest path.

Note: this cannot handle negative weights, one algorithm that can handle though is the `Bellman-Ford Algorithm`

![image](https://user-images.githubusercontent.com/111989096/192417505-174af56f-eabb-4db0-bbac-0fdb2eeea096.png)

### Explanation:
Since `start -> b -> a -> fin` has the least amout of weight compared to any other combination, this is the shortest path.
