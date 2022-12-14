# Dijktra's Algorithm
# Worst Case: O(V^2)

def dijkstra():
    node = find_lowest_cost_node(costs)

    while node is not None:
        cost = costs[node]
        neighbors = graph[node]

        for n in neighbors.keys():
            new_cost = cost + neighbors[n]

            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node

        processed.append(node)
        node = find_lowest_cost_node(costs)

    print_output()


# Find the lowest cost node
def find_lowest_cost_node(costs):
    lowest_cost = infinity
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]

        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


# Print the path from start to fin
def print_output():
    parent = "fin"
    path = ["fin"]

    while parent != "start":
        path.append(parents[parent])
        parent = parents[parent]

    path.reverse()
    print(" -> ".join(path))


# Graph
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}


# Costs Hash Map
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity


# Parents Hash Map
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None


# Processed Array (Will be used to store the nodes that have been processed)
processed = []

dijkstra()
# Output
# start -> b -> a -> fin