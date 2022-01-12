class Node:
    def __init__(self,val):
        self.val = val
        self.left =None
        self.right = None
def findMaxNode(root):
    if root is None:
        return 0
    leftMax = findMaxNode(root.left)
    rightMax = findMaxNode(root.right)
    return max(root.val, leftMax, rightMax)

def sumOfNodes(root):
    if root is None:
        return 0
    leftSum = sumOfNodes(root.left)
    rightSum = sumOfNodes(root.right)
    return (root.val + leftSum + rightSum)

def heightOfTree(root):
    if root is None:
        return -1 # -1 for edges and 0 for nodes
    leftHeight = heightOfTree(root.left)+1 
    rightHeight = heightOfTree(root.right)+1
    return max(leftHeight,rightHeight)

if __name__=="__main__":
    root= Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    print(findMaxNode(root))
    print(sumOfNodes(root))
    print(heightOfTree(root))