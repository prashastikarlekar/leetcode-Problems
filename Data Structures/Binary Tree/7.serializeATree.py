class Node:
    def __init__(self,val):
        self.val = val
        self.left= None
        self.right = None 

def serialize(root):
    if root is None:
        return 'X'
    left = serialize(root.left)
    right = serialize(root.right)
    return str(root.val) + ','+ str(left) + ',' + str(right) 

if __name__=="__main__":
    root= Node(1)
    root.left =Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(5)
    print(serialize(root))

    
