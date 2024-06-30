def bellman_ford():

    graph = {
        'a': {'b': -1, 'e': 6},
        'b': {'c': 3, 'd': 2},
        'c': {'b': 5, 'd': 4, 'e': 2},
        'd': {'e': 1},
        'e': {'a': 7}
    }

    vertices = list(graph.keys())

    dist = {v: float('inf') for v in vertices}
    dist['a'] = 0

    for _ in range(len(vertices) - 1):
        for u in vertices:
            for v in graph[u]:
                dist[v] = min(dist[v], dist[u] + graph[u][v])

    print(dist)

    for u in vertices:
        for v in graph[u]:
            if dist[v] > dist[u] + graph[u][v]:
                print('Negative edge cycle detected')
                return

    print('No negative edge cycle detected')

    return


if __name__ == "__main__":
    bellman_ford()

