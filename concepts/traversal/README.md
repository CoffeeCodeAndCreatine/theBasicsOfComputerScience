# Tree Traversals

## What?
"Traversals" or "Tree Traversals" is a way to explore or search though any given tree or graph. Generally speaking BFS and DFS meaning breadth first search and depth first search are the two most common forms of traversal.

## Why
Quite a few things in computer science are stored in graphs or trees, being able to explore these or find an item in a efficient manor is an invaluable skill to have.

## Examples
Lets say you have the tree of the following form
```bash
    1
   -|-
  |   |
  2   3
 -|-
|   |
4   5
```
Visiting all the nodes using BFS would yield: 1,2,3,4,5
Visiting all the nodes using DFS (preorder) would yield: 1,2,4,5,3
Visiting all the nodes using DFS (inorder) would yield: 4,2,5,3,1
Visiting all the nodes using DFS (postorder) would yield: 4,5,2,3,1

##Run Time
Each one of these traversals will require O(n) as they visit each node once. 

##Space
At a high level extra space is required for Level Order Traversals O(w) where w is the width of the tree, and Depth First Traversals O(h) where h is the height of the tree.

##When to use each?
At a high level DFS typically performs better when starting from a root, where BFS typically performs better when starting from a leaf.
If space requirements are no issue, consider where the problem starts. 
