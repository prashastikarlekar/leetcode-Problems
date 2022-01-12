# binary tree is a tree whose elements have at most 2 children, we call them left and right node
# a tree node contains the following parts- Data, pointer to the left child, pointer to the right child
# code to implement a binary tree
class Node:
    def __init__(self,key):
        self.val=key
        self.left= None
        self.right= None

# Code to create a binary tree with our class node
# first we create a root node
root= Node(1)
# now the tree looks like this   1
#                           None    None
# to add more nodes to this tree
root.left = Node(2)
root.right= Node(3)
#               1
#         2             3
#    None   None   None   None
root.left.left= Node(4) # left child added to the node 2
# maximum number of nodes at level L = 2^L
# level of root is 0