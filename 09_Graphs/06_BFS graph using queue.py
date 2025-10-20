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


# mix both creating graph and also presented graph

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
        lst.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:

                visited.add(neighbor)
                queue.append(neighbor)

        
    print(lst)

# or for adj means already having graph like adj = [[2, 3, 1], [0], [0, 4], [0], [2]]

def bfs_v2(adj):

    V = len(adj)
    visited = [False] * V
    queue = deque([0])
    visited[0] = True
    lst = []

    while queue:
        node = queue.popleft()
        lst.append(node)

        for neighbor in adj[node]:
            if  not visited[neighbor]:

                visited[neighbor] = True
                queue.append(neighbor)

        
    print(lst)

edges = [[0,1],[0,2],[1,3],[2,3]]
graph = create_graph(edges)
print(graph)

print("\nBFS")
bfs(graph,0)


print("\nBFS_v2")
adj = [[2, 3, 1], [0], [0, 4], [0], [2]]
bfs_v2(adj)


