class Node:
    def __init__(self,val):
        self.val =val
        self.left= None
        self.right= None

def fDate(dates):
    res= []
    map = {'Jan':'01','Feb':'02'}
    for date in dates:
        dateList = date.split(" ")
        d = str('0'+ dateList[0][:1]) if len(date) ==12 else str(dateList[0][:2])
        for m in map:
            if m == dateList[1]:
                month = str(map[m])
        year = str(dateList[-1])
        result = year + '-' + month+'-'+d
        res.append(result)
    return res

def preorder(root):
    stack = [root]
    res= []
    while stack:
        current= stack.pop()
        res.append(current.val)
        if current.right: stack.append(current.right)
        if current.left: stack.append(current.left)

    return res


if __name__=="__main__":
    dates = ['26th Feb 1980', '2nd Jan 2098']
    print(fDate(dates))
    root= Node(4)
    root.left = Node(2)
    root.right =Node(8)
    root.right.left = Node(5)
    root.right.right= Node(10)
    root.right.left.right = Node(7)
    root.right.left.right.left = Node(6)
    print(preorder(root))



