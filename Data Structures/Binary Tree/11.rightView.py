from collections import deque

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
def rightView(root):
    output =[]
    if root is None:
        return output
    queue =[]
    current = root
    while current:
        queue.append(current)
        # current = stack.pop()
        output.append(current.val)
        
        if current.right:
            # print("its in if")

            current = current.right
        # jese hi right subtree khatam hogi i.e once you reach right leave, you need to trace back to its parent and iterate over left
        # subtree' s right view
        else:
            if current.left:
                print("its in if")
                current = current.left
            else: # is else me tabhi aaega jab poora right khatam ho gaya hai
                print("its in else 1")

                if not current.right: current = None# this case is when we hit the right leaf of the tree
                # now we need to traverse the left subtree
                else:
                    print("its in else 2")
                    node = queue[-2]
                    print(node)
                    if node.left:
                        if node.left.right:
                            current = node.left.right
                        else:
                            current = node.left.left

    return output
    

def rightViewBFS(root):
    output = []
    if root is None:
        return output
    queue = deque([root])
    level = 0
    while queue:
        levelLength = len(queue)
        output.append([])
        for i in range(levelLength):
            node = queue.popleft()
            output[level].append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        level+=1
    return [i[-1] for i in output]


if __name__=="__main__":
    # a= Node('a')
    # b= Node('b')
    # c= Node('c')
    # d= Node('d')
    # e= Node('e')
    # f= Node('f')
    # a.left = b
    # a.right= c
    # b.left = d
    # b.right = e
    # c.left = f
    root= Node(1)
    root.left =Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    # root.right.right = Node(4)
    print(rightViewBFS(root))