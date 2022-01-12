from collections import deque
class Node:
    def __init__(self,val):
        self.val = val
        self.left= None
        self.right= None

def leftClonedTree(root):
    if root is None:
        return 
    leftClonedTree(root.left)
    leftClonedTree(root.right)
    leftNode = Node(root.val)
    leftNode.left, leftNode.right = root.left, None
    root.left, root.right = leftNode, root.right
    return bfs(root)
    
def transformBack(root):
    if root is None:
        return 
 
    if root.left:
        root.left = root.left.left
    # root.right= root.right
    transformBack(root.left)
    transformBack(root.right)

    return bfs(root)


def bfs(root):
    queue = deque([root])
    levels, level = [], 0
    while queue:
        levelLength = len(queue)
        levels.append([])
        for _ in range(levelLength):
            node= queue.popleft()
            levels[level].append(node.val)
            if node.left : queue.append(node.left)
            if node.right: queue.append(node.right)
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
    print(transformBack(root))