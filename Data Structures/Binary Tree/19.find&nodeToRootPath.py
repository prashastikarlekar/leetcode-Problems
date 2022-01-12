# find a given node in the tree and print the node tracing its path to the root
class Node:
    def __init__(self,val):
        self.val = val 
        self.left = None
        self.right = None

path = []
def findAndRootToPath(root, node):
    if root is None:
        return 0
    if root.val ==node:
        path.append(root.val)
        return True
    foundInLeft = findAndRootToPath(root.left, node)
    if foundInLeft:
        path.append(root.val)
        return True
    foundInRight = findAndRootToPath(root.right, node)
    if foundInRight:
        path.append(root.val)
        return True
    return False
if __name__=="__main__":
    root= Node(50)
    root.left = Node(40)
    root.right= Node(45)
    root.left.left = Node(34)
    root.left.right = Node(30)
    root.left.right = Node(37)
    findAndRootToPath(root, 34)
    print(path)