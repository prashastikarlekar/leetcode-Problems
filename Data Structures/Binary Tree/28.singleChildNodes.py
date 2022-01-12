# will return the nodes whose parent has only one child
#        50
#       / \
#     25   75
#    / \   /
#   12 37 67
#     /  /
#    30  60     output= [30,60,67]
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right= None

def singleChildNodes(root):
    if root is None: return
    singleChildNodes(root.left)
    singleChildNodes(root.right)
    if root.left is None: 
        leftVal=0
    else: 
        leftVal = 1
    if root.right is None:
        rightVal = 0
    else:
        rightVal=1
    if leftVal ^ rightVal:
        if root.left: print(root.left.val)
        if root.right: print(root.right.val)
        return True
    return False
if __name__=="__main__":
    root= Node(50)
    root.left = Node(25)
    root.right = Node(75)
    root.left.left = Node(12)
    root.left.right= Node(37)
    root.left.right.left = Node(30)
    root.right.left = Node(67)
    root.right.left.left = Node(60)
    singleChildNodes(root)