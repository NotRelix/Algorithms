# Breadth First Search
# Worst Case: O(V + E)          <-- where V is the number of vertices and E is the number of edges

from collections import deque           # We need this to use the deque() function

def breadth_first_search(name):
    search_queue = deque()              # Creates a new queue
    search_queue += graph[name]
    searched = []                       # This array keeps track on people who are already searched

    while search_queue:
        person = search_queue.popleft()         # Grabs the first person off the queue

        if person not in searched:
            if person_is_seller(person):
                print(f"{person} is a Mango seller!")
                return True
            else:
                search_queue += graph[person]   
                searched.append(person)         

    print("No Mango sellers found")
    return False

# Our mango seller ends with a letter "m" in their name
def person_is_seller(person):
    return person[-1] == "m"

# Graphs
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["alice"] = ["peggy"]
graph["bob"] = ["anuj", "peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

# Test Cases:
breadth_first_search("you")         # thom is a Mango Seller!
breadth_first_search("bob")         # No Mango sellers found
