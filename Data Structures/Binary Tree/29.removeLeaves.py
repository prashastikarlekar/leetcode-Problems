# remove leaves in a binary tree
from collections import deque
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def removeLeaves(root):
    if root is None:
        return
    if root.left is None and root.right is None: return False
    left = removeLeaves(root.left)
    right = removeLeaves(root.right)
    if not left :
        root.left =None
    if not right:
        root.right = None
    return bfs(root)
def bfs(root):
    if root is None:
        return
    queue= deque([root])
    levels, level =[], 0
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

if __name__=="__main__":
    root = Node(50)
    root.left = Node(25)
    root.right = Node(75)
    root.left.left = Node(12)
    root.left.right = Node(37)
    root.right.left = Node(62)
    root.right.left.right = Node(70)
    root.right.right =Node(87)

    print(bfs(root))
    print(removeLeaves(root))