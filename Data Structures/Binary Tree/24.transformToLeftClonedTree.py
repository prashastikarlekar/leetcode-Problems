# transform tree to a left cloned tree
from collections import deque
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right= None

def leftClonedTree(root):
    if root is None:
        return 
    leftClonedTree(root.left)
    leftClonedTree(root.right)
    leftNode = Node(root.val)
    leftNode.left= root.left
    leftNode.right= None
    root.left = leftNode
    root.right = root.right
    return bfs(root)

def bfs(root):
    queue= deque([root])
    level=0
    levels =[]
    while queue:
        levelLength = len(queue)
        levels.append([])
        for _ in range(levelLength):
            node = queue.popleft()
            levels[level].append(node.val)
            if node.left : queue.append(node.left)
            if node.right : queue.append(node.right)
        level+=1
    return levels


if __name__=="__main__":
    root= Node('a')
    root.left= Node('b')
    root.right = Node('c')
    root.left.left= Node('d')
    root.left.right= Node('e')
    root.right.left= Node('f')
    root.right.right= Node('g')
    print(leftClonedTree(root))
    # print(bfs(root))
