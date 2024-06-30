def dfs(tree, start, visited=None, dfs_order=None):
    if visited is None:
        visited = set()
    if dfs_order is None:
        dfs_order = []

    visited.add(start)
    dfs_order.append(start)

    for neighbor in tree[start]:
        if neighbor not in visited:
            dfs(tree, neighbor, visited, dfs_order)

    return dfs_order

if __name__ == "__main__":
    # Tree structure based on provided example
    tree = {1: [2, 3], 2: [5], 3: [4, 6], 4: [], 5: [2, 7, 10, 13], 6: [3, 7], 7: [5, 6, 8, 9], 8: [7], 9: [7, 12], 10: [5, 11], 11: [10], 12: [9, 13], 13: [5, 12]}
    print("Tree structure:", tree)
    start_node = 1  # Starting node for DFS
    dfs_result = dfs(tree, start_node)
    print("DFS Traversal Order:", dfs_result)
