# given a a target , find out if its in the tree or not
from collections import deque
class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def dfsFind(root, target):
    if root is None:
        return False
    stack= [root]
    while stack:
        current = stack.pop()
        if current.val == target:
            return True
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    
    return False

def bfsFind(root, target):
    if root is None:
        return False
    queue = deque([root])
    while queue:
        current= queue.popleft()
        if current.val == target:
            return True
        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)
    return False

def dfsRecursive(root,target):
    if root is None:
        return False
    if root.val == target:
        return True
    left = dfsRecursive(root.left,target)
    right = dfsRecursive(root.right, target)
    return left or right


if __name__=="__main__":
    root= Node(1)
    root.left= Node(2)
    root.right=  Node(3)
    print(dfsFind(root, 0))
    print(bfsFind(root, 2))
    print(dfsRecursive(root, 2))
