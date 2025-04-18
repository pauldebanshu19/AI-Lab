def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

def get_graph():
    graph = {}
    nodes = int(input("Enter the number of nodes: "))
    
    for _ in range(nodes):
        node = input("Enter node: ")
        neighbors = input(f"Enter neighbors of {node} (comma-separated): ").split(',')
        graph[node] = set(neighbors) if neighbors != [''] else set()
    return graph

graph = get_graph()
start_node = input("Enter start node for DFS: ")
print("DFS Traversal:")
dfs(graph, start_node)
