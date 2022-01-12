# code to implement the insertion of a node in the linked list
class Node:
    def __init__(self,data):
        self.data =data
        self.next = None
class LinkedList:
    def __init__(self) :
        self.head = None
    def printElements(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    def insertANode(self,previousNode, new_data): # function to add a new node after the given previous node
        nodeToBeInserted = Node(new_data)
       
        nodeToBeInserted.next = previousNode.next # firstly link the new node's next to point towards the next node
        previousNode.next = nodeToBeInserted               
            
        
        
if __name__=="__main__":
    firstNode = Node(10)
    secondNode = Node(11)
    thirdNode =Node(12)
    forthNode= Node(13)
    fifthNode = Node(14)
    llist = LinkedList()
    llist.head = firstNode
    firstNode.next = secondNode
    secondNode.next = thirdNode
    thirdNode.next = forthNode
    forthNode.next = fifthNode
    llist.printElements()
    llist.insertANode(fifthNode, 15)
    llist.printElements()



        

        
