from collections import deque
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right=  None

def zigzag(root):
    output = []
    if root is None:
        return output
    level =0
    queue = deque([root])
    while queue:
        output.append([])
        levelLength = len(queue)
        for i in range(levelLength):
            node = queue.popleft()
            output[level].append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level+=1
    for i in output:
        if output.index(i)%2 !=0:
            i.reverse()
    return output

if __name__=="__main__":
    root= Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)
    print(zigzag(root))

        