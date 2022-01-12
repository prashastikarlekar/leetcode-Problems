# flatten a binary tree to a linked list , it should be in pre-order form
class Node:
    def __init__(self,val):
        self.val = val 
        self.left = None
        self.right = None
class LLNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        
def flattenToLinkedList(root):
    if root is None:
        return 
    # print(root.val)
    # left = flattenToLinkedList(root.left)
    # right = flattenToLinkedList(root.right)
    # if root.left and root.right is None:
    #     node.next = LLNode(root.left.val)
    # if root.right and root.left is None:
    #     node.next = LLNode(root.right.val)
    # if root.left and root.right:
    #     node.next = LLNode(root.left.val)
    #     node.next.next = LLNode(root.right.val)
    leftNode = flattenToLinkedList(root.left)
    node = LLNode(root.val)
    temp = leftNode
    while(temp):
        temp = temp.next
    rightNode = flattenToLinkedList(root.right)
    node.next = rightNode
    return node

if __name__=="__main__":
    root= Node(1)
    root.left = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right=  Node(5)
    root.right.right = Node(6)
    print(flattenToLinkedList(root))