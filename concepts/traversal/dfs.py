class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def print_dfs_inorder(root_node):
    if root_node is not None:
        print_dfs_inorder(root_node.left)
        print(root_node.data)
        print_dfs_inorder(root_node.right)


def print_dfs_preorder(root_node):
    if root_node is not None:
        print(root_node.data)
        print_dfs_preorder(root_node.left)
        print_dfs_preorder(root_node.right)


def print_dfs_postorder(root_node):
    if root_node is not None:
        print_dfs_postorder(root_node.left)
        print_dfs_postorder(root_node.right)
        print(root_node.data)


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
    print("Running examples of dfs inorder")
    print_dfs_inorder(root)
    print("Running examples of dfs preorder")
    print_dfs_preorder(root)
    print("Running examples of dfs postorder")
    print_dfs_postorder(root)


if __name__ == "__main__": main()
