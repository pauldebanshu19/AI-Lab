from collections import deque

def bfs(graph, start):
    visited = set()  
    queue = deque([start])  

    while queue:
        node = queue.popleft()  
        if node not in visited:
            print(node, end=" ")  
            visited.add(node)  
            queue.extend(graph[node]-visited)  

# Taking input for the graph
def get_graph():
    graph = {}
    nodes = int(input("Enter the number of nodes: "))
    for _ in range(nodes):
        node = input("Enter node : ")
        neighbors = input(f"Enter neighbors of {node} (comma-separated): ").replace(" "," ").split(',')
        graph[node] = set(neighbors) if neighbors != [''] else set()
    
    return graph

graph = get_graph()
start_node = input("Enter start node for BFS: ")
print("BFS Traversal:")
bfs(graph, start_node)