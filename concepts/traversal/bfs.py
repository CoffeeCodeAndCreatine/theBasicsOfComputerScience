class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def print_level_order_recursive(root_node):
    node_height = calc_node_height(root_node)
    for i in range(1, node_height + 1):
        print_given_level(root_node, i)


def print_level_order_iterative(root_node):
    if root_node is None:
        return

    queue = []
    queue.append(root_node)

    while len(queue) > 0:
        print(queue[0].data)
        root_node = queue.pop(0)

        if root_node.left is not None:
            queue.append(root_node.left)

        if root_node.right is not None:
            queue.append(root_node.right)


def print_given_level(root_node, level):
    if root_node is None:
        return
    if level == 1:
        print(str(root_node.data))
    elif level > 1:
        print_given_level(root_node.left, level - 1)
        print_given_level(root_node.right, level - 1)


def calc_node_height(node):
    if node is None:
        return 0
    else:
        left_height = calc_node_height(node.left)
        right_height = calc_node_height(node.right)

        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1


def create_sample_tree():
    """
    sample tree follows the form
         1
        -|-
       |   |
       2   3
      -|-
     |   |
     4   5

    """

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    return root


def main():
    print("creating sample tree")
    root = create_sample_tree()
    print("Running examples of BFS with recursion")
    print_level_order_recursive(root)
    print("Running examples of BFS with iteration")
    print_level_order_iterative(root)


if __name__ == "__main__": main()
