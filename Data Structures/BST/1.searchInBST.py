class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

output = []
def search(root,val):
    if root is None:
        return output
    if root.val == val:
        output.append(root.val)
        if root.left: search(root.left, root.left.val)
        if root.right: search(root.right, root.right.val)
    if root.left :
        search(root.left, val)
    if root.right:
        search(root.right, val)
    return output

if __name__=="__main__":
    root= Node(4)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(3)
    print(search(root, 2))