# code to check if a binary tree is symmetric or not

class Node:
    def __init__(self,val):
        self.val = val
        self.left= None
        self.right= None

def isSymmetric(root):
    if root is None:
        return True
    return check(root.left,root.right)
def check(leftSubtree,rightSubtree):
    if leftSubtree is None and rightSubtree is None:
        return True
    elif leftSubtree and rightSubtree:
        return leftSubtree.val == rightSubtree.val and check(leftSubtree.left,rightSubtree.right) and check(leftSubtree.right, rightSubtree.left)
        


if __name__=="__main__":
    root= Node(1)
    root.left = Node(2)
    root.right= Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.right= Node(3)
    (isSymmetric(root))
