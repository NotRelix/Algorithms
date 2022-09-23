# Breadth First Search

> Time Complexity: O(V + E) </br>
V = Vertices and E = Edges.

### Description:
This algorithm uses a **queue** which is also called a FIFO data structure (First In, First Out). This algorithm uses graphs which first asks whether a path exists from node A to node B, if there is then find the shortest path. </br>

One thing to note is that it doesn't search for nodes that are already searched.

---

![breadth](https://user-images.githubusercontent.com/111989096/191940161-946bc6ee-33df-4ae7-b0fc-04286a0edc0d.png)

### Explanation:
1. We need to find D or F in the graph
2. First one is A
3. Second one is B
4. Third is C
5. Fourth is D, we found it so it's the shortest path

Note: We don't need to look for F since D was found first
