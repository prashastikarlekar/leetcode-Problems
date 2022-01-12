# Given the root of a binary tree, return the length of the diameter of the tree. The diameter of a binary tree is the length of the 
# longest path between any two nodes in a tree. This path may or may not pass through the root. 
# The length of a path between two nodes is represented by the number of edges between them.
from collections import deque
class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

# def diameter(root):
#     if root is None:
#         return 0
def heightOfBinaryTree(root):
    if root is None: 
        return -1  # 0 for nodes and -1 for edges
    return max(heightOfBinaryTree(root.left), heightOfBinaryTree(root.right)) +1 


def diameterRecursive(root):
    # we have 3 factors competing in this problem
    # 1. when diameter exists between two nodes both on LHS - leftDiameter
    # 2. when diamter exists between two nodes both on RHS - rightDiameter
    # 3. when diamter exists between left subtree's deepest and right subtree's deepest nodes i.e it is based on root node
    if root is None: return 0
    # leftDiameter is the maximum distance between 2 nodes on LHS i.e when diameter of tree (both end nodes)is present on LHS of tree
    leftDiameter= diameterRecursive(root.left)
    # rightDiameter is the max distance between 2 nodes on RHS i.e when dia of tree(both end nodes) is on RHS of tree
    rightDiameter = diameterRecursive(root.right)
    # third factor
    factor3= heightOfBinaryTree(root.left) + heightOfBinaryTree(root.right) +2 # +2 isliye kiya because root ki 2 edges
    return max(max(leftDiameter, rightDiameter), factor3)


if __name__=="__main__":
    root= Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right= Node(5)
    # print(diameter(root))
    print(diameterRecursive(root))  