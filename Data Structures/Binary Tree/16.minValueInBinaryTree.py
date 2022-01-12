# find th eminimum node in the tree
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right= None


def minValueOfNode(root):
    if root is None:
        return 0
    stack,min = [root], root.val
    while stack:
        current = stack.pop()
        if current.val < min:
            min= current.val
        if current.left:stack.append(current.left)
        if current.right: stack.append(current.right)
    return min

# min se bada but baki sabse chhota       min < secondMin < all
def findSecondMinimum(root):
    if root is None: return 0
    stack, visistedNodes = [root],[]
    min,secondMin= root.val,root.val
    while stack:
        current = stack.pop()
        if current.val < min:
            min= current.val
        visistedNodes.append(current.val)
        if current.left:stack.append(current.left)
        if current.right: stack.append(current.right)
    return visistedNodes   

def minRecursive(root):
    if root is None: return float('inf')
    return min( minRecursive(root.left), minRecursive(root.right))

if __name__=="__main__":
    root= Node(5)
    root.left= Node(4)
    root.right = Node(11)
    root.left.left= Node(8)
    root.left.right= Node(11)
    root.right.right = Node(3)
    print(minValueOfNode(root))
    # print(findSecondMinimum(root))
    print(minRecursive(root))