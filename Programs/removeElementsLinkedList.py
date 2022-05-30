# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return 
# the new head.
class Node:
    def __init__(self,data) :
        self.data =data
        self.next =None
class LinkedList :
    def __init__(self) :
        self.head = None
    def printElements(self):
        while self.head:
            print(self.head.data)
            self.head = self.head.next
        
if __name__=="__main__":
    llist= LinkedList()
    firstNode = Node(1)
    secondNode = Node(2)
    thirdNode = Node(6)
    forthNode =Node(3)
    fifthNode= Node(4)
    sixthNode =Node(5)
    seventhNode =Node(6)
    llist.head = firstNode
    firstNode.next = secondNode
    secondNode.next = thirdNode
    thirdNode.next = forthNode
    forthNode.next  =fifthNode
    fifthNode.next = sixthNode
    sixthNode.next = seventhNode

    value = 6
    dummyNode = Node(0)
    dummyNode.next = llist
    previous = dummyNode
    current= llist.head
    llist.printElements()
    while(current):
        if current.data ==value:
            previous.next = current.next
        else:
            previous = current
        current= current.next
    dummyNode.next.printElements() 
    

        
        
        