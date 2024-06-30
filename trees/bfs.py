from collections import deque

def bfs(tree, start):
    visited = set()
    queue = deque([start])
    bfs_order = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            bfs_order.append(node)
            for child in tree[node]:
                if child not in visited:
                    queue.append(child)

    return bfs_order

if __name__ == "__main__":
    # Tree structure based on provided example
    tree = {1: [2, 3], 2: [5], 3: [4, 6], 4: [], 5: [2, 7, 10, 13], 6: [3, 7], 7: [5, 6, 8, 9], 8: [7], 9: [7, 12], 10: [5, 11], 11: [10], 12: [9, 13], 13: [5, 12]}
    print("Tree structure:", tree)
    start_node = 1  # Starting node for BFS
    bfs_result = bfs(tree, start_node)
    print("BFS Traversal Order:", bfs_result)
