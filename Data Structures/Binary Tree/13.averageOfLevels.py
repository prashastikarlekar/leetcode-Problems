# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
from collections import deque
class Node:
    def __init__(self,val):
        self.val = val
        self.left  =None
        self.right = None


def averageOfLevels(root):
    # first we traverse level by level
    levels = []
    output= []
    level  =0 
    if root is None:
        return levels
    queue = deque([root])
    
    while queue:
        sum =0
        count = 0
        levels.append([])
        levelLength = len(queue)
        for _ in range(levelLength):
            node = queue.popleft()
            sum+=node.val
            count+=1
            print(sum)
            print(count)
            levels[level].append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        output.append(sum/count)
        level+=1
    # at this point of time we have the arrays of the values on each level of the tree
    # for i in levels:
    #     sum=0
    #     count=0
    #     for j in i:
    #         sum+=j
    #         count+=1
    #     output.append(sum/count)
    return output


if __name__=="__main__":
    root = Node(3)
    root.left =Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right =Node(7)
    # [3.0, 9 + 20 /2 = 14.5 , 15+7 /2 = 11]
    print(averageOfLevels(root))