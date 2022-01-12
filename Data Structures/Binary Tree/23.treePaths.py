# Given the root of a binary tree, return all root-to-leaf paths in any order.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right =None
# output= []
def allRootToLeafPaths(root,path,output):
    # output= []
    if root is None:
        return 0
    if root.left is None and root.right is None:
        path =path + "->" if path!="" else "" 
        path+= str(root.val)
        output.append(path)
        # print(path)
        # print(output)
    path = path + "->" if path != "" else ""        
    allRootToLeafPaths(root.left, path + str(root.val),output)
    allRootToLeafPaths(root.right, path + str(root.val), output)
    return output

if __name__ == "__main__":
    root = Node(50)
    root.left = Node(25)
    root.right = Node(75)
    root.left.left = Node(12)
    root.left.right = Node(37)
    root.left.right.left = Node(30)
    root.left.right.right = Node(40)
    root.right.left = Node(62)
    root.right.right = Node(87)
    root.right.left.left = Node(60)
    root.right.left.right = Node(78)
    print(allRootToLeafPaths(root, "",[]))
   