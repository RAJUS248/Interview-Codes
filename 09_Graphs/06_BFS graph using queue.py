from collections import defaultdict,deque

def create_graph(edges):

    graph = defaultdict(list)

    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)

    return dict(graph)

def bfs(graph,start):
    
    visited = set()
    queue = deque([start])
    visited.add(start)
    lst = []

    while queue:
        node = queue.popleft()
        

        for neighbor in graph[node]:
            if neighbor not in visited:

                visited.add(neighbor)
                queue.append(neighbor)

        lst.append(node)
    print(lst)


edges = [[0,1],[0,2],[1,3],[2,3]]
graph = create_graph(edges)
print(graph)

print("BFS")

graph = bfs(graph,0)
