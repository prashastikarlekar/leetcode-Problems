# remove all the leaves from the binary tree with a given target value i.e only those leaves with the value of target need to be deleted
from collections import deque
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
def bfs(root):
    if root is None: return 
    queue = deque([root])
    levels, level = [], 0
    while queue:
        levelLength = len(queue)
        levels.append([])
        for _ in range(levelLength):
            node = queue.popleft()
            levels[level].append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        level+=1
    return levels

def removeLeavesWithTarget(root, target):
    if root is None:
        return None
    root.left = removeLeavesWithTarget(root.left, target)
    root.right = removeLeavesWithTarget(root.right, target)
    
    if root is not None and root.left is None and root.right is None and root.val == target:
        return None
    else:
        return root
    # return bfs(root)

if __name__=="__main__":
    # root= Node(1)
    # root.left =Node(2)
    # root.right = Node(3)
    # root.left.left = Node(2)
    # root.right.left = Node(2)
    # root.right.right = Node(4)

    # root = Node(1)
    # root.left = Node(2)
    # root.left.left = Node(2)
    # root.left.left.left= Node(2)

    root = Node(1)
    root.left = Node(3)
    root.right = Node(3)
    root.left.left = Node(3)
    root.left.right=  Node(2)


    print(removeLeavesWithTarget(root, 3))
    print(bfs(root))