class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right =None

path = [] # to store the path from the node to the root

def nodeToRoot(root, node):
    if root is None:
        return False
    if root.val == node.val:
        path.append(root)
        return True
    foundInLeft = nodeToRoot(root.left, node)
    if foundInLeft :
        path.append(root)
        return True
    foundInRight = nodeToRoot(root.right, node)
    if foundInRight:
        path.append(root)
        return True
    return False

def printKLevelsDown(root, k, blocker):
    if root is None or k < 0 or root.val == blocker:
        return 0
    if k == 0:
        print(root.val)
    printKLevelsDown(root.left, k-1, blocker)
    printKLevelsDown(root.right, k-1,blocker)

def printKLevelsFar(root, k):
    if root is None or k <0:
        return 0
    for i in range(len(path)):
        printKLevelsDown(path[i], k-i, path[i-1])


if __name__=="__main__":
    root= Node(3)
    root.left = Node(5)
    root.right = Node(1)
    root.left.left = Node(6)
    root.left.right = Node(2)
    root.left.right.left = Node(7)
    root.left.right.right = Node(4)
    root.right.left = Node(0)
    root.right.right = Node(8)
    print(nodeToRoot(root, root.right))
    print(path)
    printKLevelsDown(root, 1 ,5)
    printKLevelsFar(root, 2)