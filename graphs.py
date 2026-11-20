graph = [
    [0, 1, 0, 1, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0]
]


def dfs(graph, start):
    visited = []
    result = []

    def visit(v):
        visited.append(v)
        result.append(v)

        for i in range(len(graph)):
            if graph[v][i] == 1 and i not in visited:
                visit(i)

    visit(start)
    return result

print("DFS от вершины 0:", dfs(graph, 0))
print("DFS от вершины 4:", dfs(graph, 4))


def bfs(graph, start):
    visited = []
    result = []
    queue = []

    visited.append(start)
    queue.append(start)

    while len(queue) > 0:
        v = queue.pop(0)
        result.append(v)

        for i in range(len(graph)):
            if graph[v][i] == 1 and i not in visited:
                visited.append(i)
                queue.append(i)

    return result

print("BFS от вершины 0:", bfs(graph, 0))
print("BFS от вершины 4:", bfs(graph, 4))


weighted_graph = [
    [0, 4, 0, 2, 9, 0, 0, 0],
    [4, 0, 3, 0, 0, 0, 0, 0],
    [0, 3, 0, 8, 0, 0, 4, 0],
    [2, 0, 8, 0, 0, 6, 0, 0],
    [9, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 6, 1, 0, 0, 3],
    [0, 0, 4, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 3, 2, 0]
]

def dijkstra(graph, start, finish):
    n = len(graph)
    distances = [float('inf')] * n
    visited = [False] * n
    previous = [-1] * n
    distances[start] = 0
    
    for _ in range(n):
        min_dist = float('inf')
        v = -1
        for i in range(n):
            if not visited[i] and distances[i] < min_dist:
                min_dist = distances[i]
                v = i
        if v == -1:
            break
        
        visited[v] = True
        for i in range(n):
            if graph[v][i] > 0 and not visited[i]:
                new_dist = distances[v] + graph[v][i]
                if new_dist < distances[i]:
                    distances[i] = new_dist
                    previous[i] = v

    if distances[finish] == float('inf'):
        return float('inf'), []

    path = []
    current = finish
    while current != -1:
        path.append(current)
        current = previous[current]

    path.reverse()

    return distances[finish], path

print("Путь 0 -> 7:", dijkstra(weighted_graph, 0, 7))
print("Путь 2 -> 4:", dijkstra(weighted_graph, 2, 4))


def shortest_path_bfs(graph, start, finish):
    n = len(graph)
    visited = [False] * n
    previous = [-1] * n
    queue = []

    visited[start] = True
    queue.append(start)
    while len(queue) > 0:
        v = queue.pop(0)
        if v == finish:
            break
        
        for i in range(n):
            if graph[v][i] == 1 and not visited[i]:
                visited[i] = True
                previous[i] = v
                queue.append(i)

    if not visited[finish]:
        return []

    path = []
    current = finish
    while current != -1:
        path.append(current)
        current = previous[current]

    path.reverse()
    return path

print("0 -> 7:", shortest_path_bfs(graph, 0, 7))
print("1 -> 5:", shortest_path_bfs(graph, 1, 5))
print("2 -> 4:", shortest_path_bfs(graph, 2, 4))

pairs = [(0, 7), (1, 5), (2, 4)]
for start, finish in pairs:
    path = shortest_path_bfs(graph, start, finish)
    distance, dijkstra_path = dijkstra(graph, start, finish)

    print("Пара:", start, "->", finish)
    print("Маршрут BFS:", path)
    print("Количество рёбер:", len(path) - 1)
    print("Расстояние Дейкстры:", distance)