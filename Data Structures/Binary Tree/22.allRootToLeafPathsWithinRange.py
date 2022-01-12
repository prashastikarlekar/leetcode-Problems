# return all the paths with root to leaves where the sum of the values in the path falls between a given range
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right= None
path =[]
def rootToNodePath(root, path, sum, low,high):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        sum +=root.val
        if sum >=low and sum <=high:
            print(path + str(root.val))
        return

    rootToNodePath(root.left, path+str(root.val)+" , ", sum+root.val, low, high)
    rootToNodePath(root.right, path+str(root.val)+" , ", sum+root.val, low, high)


if __name__=="__main__":
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
    #         50
    #     25       75
    #   12 37     62  87
    #    30 40  60 78
    (rootToNodePath(root, "",0,90,200))

    