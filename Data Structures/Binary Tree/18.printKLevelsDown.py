class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right =None

def printKLevelsDown(node,k):
    if node is None or k <0:
        return None
    if k==0:
        print(node.val)
    printKLevelsDown(node.left, k-1)
    printKLevelsDown(node.right, k-1)




if __name__=="__main__":
    root= Node(50)
    root.left = Node(15)
    root.right = Node(10)
    root.left.left = Node(25)
    root.right.right = Node(20)
    printKLevelsDown(root,1)