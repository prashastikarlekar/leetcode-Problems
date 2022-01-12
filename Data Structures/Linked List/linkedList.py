# Code to implement linked list and to print all data
class Node:
    def __init__(self,data):
        self.data = data
        self.next= None
class LinkedList:
    def __init__(self):
        self.head= None
    # function to print contents of linked list
    def printLList(self):
        temp= self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    

# creating linked list
llist = LinkedList()
# creating nodes
llist.head = Node(1)
second= Node(2)
third = Node(3)
# linking them together
llist.head.next= second
second.next = third

llist.printLList()