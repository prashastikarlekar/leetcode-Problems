from collections import deque
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def invertTree(root):
        if root is None:
            return 
        invertTree(root.left)
        invertTree(root.right)
        if root.left or root.right:
            root.left, root.right = root.right, root.left
        return root

def bfs(root):
        queue= deque([root])
        levels = []
        level = 0
        while queue:
            levelLength = len(queue)
            levels.append([])
            for _ in range(levelLength):
                node = queue.popleft()
                levels[level].append(node.val)
                if node.left:queue.append(node.left)
                if node.right : queue.append(node.right)
            level+=1
        return levels


if __name__=="__main__":
    root= Node(4)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right= Node(3)
    root.right.left = Node(6)
    root.right.right = Node(9)
    invertTree(root)
    print(bfs(root))
