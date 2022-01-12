class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right =None
def inOderTraverse(root):
    
    stack,output=[],[] # we start with an empty stack and not the root because we dont want the first value in output to be the root
    current= root # starting point is our root
    while current or stack:  # stack is keeping track of nodes in the path and that need to be visisted again so we check if its None
        while current:
            stack.append(current)
            current = current.left # we want to cover the left subtree first
        current = stack.pop() # once we reach the left leaf, we start popping from the stack
        output.append(current.val) # the value of the popped node
        current = current.right # once node's left and node itself is visited, we cover its right subtree
    return output

    
    
if __name__=="__main__":
    root= Node(1)
    root.left = Node(2)
    root.right= Node(3)
    root.left.left = Node(4)
    
    print(inOderTraverse(root))
