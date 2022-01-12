from collections import deque


class Node:
    def __init__(self,val):
        self.val = val
        self.left= None
        self.right = None

def hasSum(root, target):
    if root is None:
        return 0
    stack =[root]
    while stack:
        current = stack.pop()
        if current.val == target:
            return True
        if current.left: stack.append(current.left)
        if current.right: stack.append(current.right)
        target = target- current.val
    return False

def hasSumBfs(root, target):
    if root is None:
        return False
    sum =0
    queue =deque([root])
    while queue:
        current = queue.popleft()
        sum+=current.val
        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)
    return sum ==target

def sumRecursively(root):
    if root is None:
        return 0
    left = sumRecursively(root.left)
    right = sumRecursively(root.right)
    return root.val+left+right


if __name__=="__main__":
    root = Node(5)
    root.left= Node(4)
    root.right = Node(8)
    root.left.left =Node(11)
    root.left.left.left = Node(7)
    root.left.left.right= Node(2)
    root.right.left =Node(13)
    root.right.right= Node(4)
    root.right.right.right = Node(1)
    print(hasSum(root, 55))
    print(hasSumBfs(root, 53))
    print(sumRecursively(root))