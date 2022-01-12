class Node:
    def __init__(self,val):
        self.val = val
        self.left= None
        self.right = None
path = [] # jo find kiya waha se upar root tak ka path dega so wherever its treu , we will append that value
output= []

def findNode(root, val): # will get to check nodes above the given node
    if root is None: 
        return False
    if root.val == val:
        path.append(root)
        return True
    foundInLeft = findNode(root.left,val)
    if foundInLeft:
        path.append(root)
        return True
    foundInRight = findNode(root.right, val)
    if foundInRight:
        path.append(root)
        return True
    return False
def printKLevelsDown(root, k,blocker): # will get to check nodes below 
    # to print the nodes that are k levels down from the given node
    if root is None or k<0 or root == blocker:
        return None
    if k==0 :
        output.append(root.val)
        # print(root.val)
    printKLevelsDown(root.left, k-1,blocker)
    printKLevelsDown(root.right, k-1, blocker)
    
def printKLevelsFar(root,node, k):
    # path=[]
    if findNode(root, node.val):
        # print(path)
        for i in range(len(path)):
            # while k >=0:
            if i==0:
                blocker = None
            else:
                blocker = path[i-1]              
            printKLevelsDown(path[i],k-i,blocker)
            # output.append(value)
    return output     

if __name__=="__main__":
    # root= Node(3)
    # root.left = Node(5)
    # root.right = Node(1)
    # root.left.left = Node(6)
    # root.left.right = Node(2)
    # root.left.right.left = Node(7)
    # root.left.right.right = Node(4)
    # root.right.left = Node(0)
    # root.right.right = Node(8)
    root = Node(1)
    # print(findNode(root, 5))
    # print(path)
    # (printKLevelsDown(root,2))
    print(printKLevelsFar(root, root, 3))
