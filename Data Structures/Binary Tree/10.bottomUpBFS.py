from collections import deque
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right= None
def bfs(root):
    queue= deque([root])
    level = 0
    output = []
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
    return output
def bottomUpbfs(root):
    result =bfs(root)
    result.reverse()
    return result


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
    print(bfs(a))
    print(bottomUpbfs(a))