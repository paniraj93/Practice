def travel(tree):
    if not tree:
        print("Empty tree")
        return

    # Start with the smallest node (assuming it is the root)
    root = min(tree.keys())
    stack_temp = [root]
    stack_print = []
    temp_set = set([root])  # to keep track of nodes in stack_temp
    visited = set()

    while stack_temp:
        current = stack_temp[-1]
        all_children_visited = True

        for child in tree[current]:
            if child not in visited and child not in temp_set:
                stack_temp.append(child)
                temp_set.add(child)
                all_children_visited = False
                break

        if all_children_visited:
            node = stack_temp.pop()
            temp_set.remove(node)
            visited.add(node)
            stack_print.append(node)

    print("Traversal order:", stack_print)

if __name__ == "__main__":
    # Tree structure based on provided example
    tree = {1: [2, 3], 2: [5], 3: [4, 6], 4: [], 5: [2, 7, 10, 13], 6: [3, 7], 7: [5, 6, 8, 9], 8: [7], 9: [7, 12], 10: [5, 11], 11: [10], 12: [9, 13], 13: [5, 12]}
    print("Tree structure:", tree)
    travel(tree)
    # output = 4 3 6 8 13 12 9 7 11 10