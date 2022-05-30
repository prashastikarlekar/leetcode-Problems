class Node:
    def __init__(self,key) :
        self.val= key
        self.left= None
        self.right= None
    
# root= [5,4,8,11,null,13,4,7,2,null,null,null,1]
targetSum = 22
root=5
diff= targetSum-root
if root.left ==targetSum and root.left.left == None and root.left.right==None:
    print(True)
else:
    print(False)

# 