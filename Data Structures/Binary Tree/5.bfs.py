# code to implement the breadth first traversal in a tree
from collections import deque
class Node:
    def __init__(self,val):
        self.val = val
        self.left= None
        self.right = None
# recursive approach
def breadthFirstSearch(root):
    levels = []
    def helper(root,level):
        if len(levels) == level:
            levels.append([])
        levels[level].append(root.val)
        if root.left:
            helper(root.left, level+1)
        if root.right:
            helper(root.right,level+1)
    helper(root,0)
    return levels

# iterative approach
def bfs(root):
    levels =[]
    level =0
    if not root:
        return levels
    queue = deque([root])

    while queue:
        levels.append([])
        levelLength = len(queue)
        for i in range(levelLength):
            node = queue.popleft()
            levels[level].append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level+=1
    return levels



if __name__=="__main__":
    root = Node('F')
    root.left = Node('B')
    root.right = Node('G')
    root.left.left = Node('A')
    root.left.right = Node('D')
    root.left.right.left= Node('C')
    root.left.right.right= Node('E')
    root.right.right= Node('I')
    root.right.right.left= Node('H')
    print(breadthFirstSearch(root))
    print(bfs(root))


def practicebfs(root):
    # first in first out in queue
    queue = deque([root])
    levels =[]
    level = 0
    while queue:
        levels.append([])
        levelLength = len(queue)
    
        for i in range(levelLength):
            node = queue.popleft()
            levels[level].append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        level +=1
    return levels

def practiceBFS2(root):
    queue = deque([root])
    levels=[]
    level =0
    while queue:
        levels.append([])
        levelLength = len(queue)
        for _ in range(levelLength):
            node = queue.popleft()
            levels[level].append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level+=1
    return levels
    