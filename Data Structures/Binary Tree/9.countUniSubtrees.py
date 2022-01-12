class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right= None

class Solution:
    def countUnisubtrees(self,root):
        
        if root is None:
            return 0
        self.count = 0
        self.uniCount(root)
        return self.count

    def uniCount(self,root):
        if root.left is None and root.right is None:
            self.count+=1  
            return True
        is_uni= True

        if root.left:
            is_uni = self.uniCount(root.left) and is_uni and root.left.val == root.val
        if root.right:
            is_uni = self.uniCount(root.right) and is_uni and root.right.val == root.val
        self.count+= is_uni
        return is_uni 

if __name__=="__main__":
    root= Node(5)
    root.left= Node(1)
    root.right= Node(5)
    root.right.right = Node(5)
    root.left.left =Node(5)
    root.left.right =Node(5)
    print(Solution.countUnisubtrees(self,root))

