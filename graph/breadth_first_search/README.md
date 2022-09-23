# Breadth First Search

> Time Complexity: O(V + E) </br>
V = Vertices and E = Edges.

### Description:
First, asks whether there is a path from node A to node B, if there is then what is the shortest path?

This algorithm uses the **queue** data structure. </br>

One thing to note is that it doesn't search for the nodes that are already searched, this is to avoid unnecessary searching.

![breadth](https://user-images.githubusercontent.com/111989096/191940161-946bc6ee-33df-4ae7-b0fc-04286a0edc0d.png)

### Explanation:
1. We need to find D or F in the graph
2. First one is A
3. Second one is B
4. Third is C
5. Fourth is D, we found it so it's the shortest path

We don't need to look for F since D was found first
