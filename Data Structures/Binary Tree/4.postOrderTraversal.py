from queue import deque
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right= None
def postOrderTraverse(root):
    stack,output=[root],[]
    # current =root
    while stack:
        while root: 
                if root.right != None:
                    stack.append(root.right)
                    stack.append(root)
                    root =root.left
        root = stack.pop()
        if root.right!= None and stack[len(stack)-1] == root.right:
            stack.pop()
            stack.append(root)
            root =root.right
        else:
            print(root.val)
            root= None  

        
            


    # return output



def levelOrderTraversal(root):
    queue = deque([root])
    ouptut = []
    level = 0
    while queue:
        


if __name__=="__main__":
    root= Node(1)
    root.left = Node(4)
    root.right= Node(2)
    root.right.left = Node(3)
    print(postOrderTraverse(root))