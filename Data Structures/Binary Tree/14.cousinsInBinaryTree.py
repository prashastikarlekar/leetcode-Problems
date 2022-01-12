# Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.
# Two nodes of a binary tree are cousins if they have the same depth with different parents.
# Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.
from collections import deque
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def isCousin(root, x, y):
    if root.val ==x or root.val == y:
        return False

    # logic here is to use level order traversal, but with few changes
    # when we check node.left and right, we check if left or right child are x or y, if yes we save them as our parents
    # to determine the depth, we loop through the levels and if x and y are in same element [] in levels, then
    # next up we check that their parent's values are same or not, 
    levels = []
    parents =[0] if root.val ==x or root.val ==y else []
    level = 0
    queue = deque([root])
    while queue:
        levels.append([])
        levelLength = len(queue)
        for _ in range(levelLength):
            node= queue.popleft()
            levels[level].append(node.val)
            if node.left:
                if node.left.val == x or node.left.val == y:
                    parents.append(node.val)                
                queue.append(node.left)
            if node.right:
                if node.right.val == x or node.right.val ==y:
                    parents.append(node.val)
                queue.append(node.right)
        level+=1
    # at this point in the code, we have our levels [] ready
    # now we iterate through it
    print(parents)
    if parents[0]==parents[1]: return False # both have same parent
    for i in levels:
        if x in i and y in i: # condition to check if x and y both have same depth
            return True           

    return False


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right =Node(4)
    # root.right.right = Node(5)
    print(isCousin(root,2,3))


def bfs(root):
    levels= []
    if root is None:
        return levels
    level = 0
    queue = deque([root])
    while queue:
        levelLength = len(queue)
        levels.append([])
        for _ in range(levelLength):
            node = queue.popleft()
            levels[level].append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level +=1
    return levels

def inOrder(root):
    stack, output =[], []
    if root is None:
        return output
    current =  root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
    output.append(current.val)
    current = current.right
    return output