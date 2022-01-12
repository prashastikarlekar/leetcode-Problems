class Node:
    def __init__(self,val):
        self.val = val
        self.left =None
        self.right = None

def preOrderTraversal(root):
    if root is None:
        return []
    stack,output = [root],[]
    while stack:
        root= stack.pop()
        if root is not None:
            output.append(root.val)
            
            if root.right is not None: # push right first and left second so that when we pop, the left node is retrieved
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)
    return output
   
if __name__=="__main__":
    root=Node(1)
    # root=Node(1)
    root.left = None
    # root.right = Node(2)
    # root.right.left = Node(3)
    result =[]
    print(preOrderTraversal(root))
