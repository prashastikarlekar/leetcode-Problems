from collections import deque
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def preOrderTraversal(root):
    stack, output = [root], []
    while stack:
        node = stack.pop()
        output.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return output
            

def inorderTraversal(root):
    stack, output = [], []
    current = root
    while current or stack:
        while current : # after this loop ends we have the left leaf node
            stack.append(current)
            current= current.left
        current = stack.pop()
        output.append(current.val)
        current = current.right
    return output

def postOrderTraversal(root):
    stack, output = [], []
    current = root
    while current or stack :
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        output.append(current.val)
        root = stack.pop()
        current = root.right
        stack.append(root)

def levelOrderTraversal(root):
    output = []
    level = 0
    if root is None:
        return output
    queue = deque([root])
    while queue:
        levelLength = len(queue)
        output.append([])
        for _ in range(levelLength):
            node = queue.popleft()
            output[level].append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
        level+=1
    return output
    

if __name__=="__main__":
    a= Node('a')
    b= Node('b')
    c= Node('c')
    d= Node('d')
    e= Node('e')
    f= Node('f')
    a.left = b
    a.right= c
    b.left = d
    b.right = e
    c.left = f
    print(preOrderTraversal(a))
    print(inorderTraversal(a))
    print(levelOrderTraversal(a))
#     a
#    / \
#   b   c
#  / \ /
# d  e f

