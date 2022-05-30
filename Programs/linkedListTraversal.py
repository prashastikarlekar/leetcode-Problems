# code to impelment the traversal in linked list
class Node:
    def __init__(self, data):
        self.data =data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def printElements(self):
        while(self.head):
            print(self.head.data)
            self.head = self.head.next
    def getNthNode(self,N): # function to get the nth node of the linked list
        i=1
        while(self.head and i<=N):
            if i==N:
                print(self.head.data)

            self.head = self.head.next
            i+=1


if __name__=="__main__":

    llist = LinkedList()
    firstNode =Node(10)
    secondNode = Node(11)
    thirdNode= Node(12)
    forthNode = Node(13)
    fifthNode = Node(14)
    sixthNode = Node(15)
    llist.head = firstNode
    firstNode.next = secondNode
    secondNode.next= thirdNode
    thirdNode.next = forthNode
    forthNode.next = fifthNode
    fifthNode.next = sixthNode
    # llist.printElements()
    llist.getNthNode(3)
        