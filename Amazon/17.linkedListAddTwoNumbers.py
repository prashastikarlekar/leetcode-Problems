class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def addNumbers(l1,l2):
    if l1 == None and l2 == None:
        return
    n1,n2 =[],[]
    temp = l1
    n1length,n2length=1,1
    n1.append(str(temp.val))
    while temp.next :
        temp = temp.next
        n1.append(str(temp.val))
        n1length+=1
    temp = l2
    n2.append(str(temp.val))
    while temp.next:
        temp = temp.next
        n2.append(str(temp.val))
        n2length+=1
    n1.reverse()
    n2.reverse()
    sum =int("".join(i for i in n1)) +int("".join(i for i in n2))
    sum=str(sum)
    for i in range(len(sum)):
        if i==0: 
            temp = Node(sum[i])
            head = temp

        else:
            temp.next = Node(sum[i])
            temp =temp.next
    return head
    
def printNodes(head):
    if head is None:
        return
    temp = head
    while(temp):
        print(temp.val)
        temp = temp.val

if __name__=="__main__":
    l1= Node(2)
    l1.next = Node(4)
    l1.next.next = Node(3)
    l2= Node(5)
    l2.next = Node(6)
    l2.next.next =Node(4)
    result =(addNumbers(l1,l2))
    printNodes(result)

