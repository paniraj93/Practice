def dijkstra():

    graph = {
        
        'a': {'b': 6, 'e': 7},
        'b': {'a': 6, 'c': 2, 'd': 1, 'e': 5},
        'c': {'b': 2, 'd': 5},
        'd': {'b': 1, 'c': 5, 'e': 2},
        'e': {'a': 7, 'b': 5, 'd': 2}
    }

    vertices = list(graph.keys())

    dist = {v: float('inf') for v in vertices}
    dist['a'] = 0

    for _ in range(len(vertices) - 1):
        for u in vertices:
            for v in graph[u]:
                dist[v] = min(dist[v], dist[u] + graph[u][v])

    print(dist)

    # for negative edge
    for u in vertices:
        for v in graph[u]:
            if dist[v] > dist[u] + graph[u][v]:
                print('Negative edge cycle detected')
                return

    print('No negative edge cycle detected')

dijkstra()
