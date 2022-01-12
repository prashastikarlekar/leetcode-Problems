# Code to implement insertion in linked list
class Node:
    def __init__(self,data):
        self.data= data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head= None

    def push(self, new_data1): # to insert at the front of the linked list
        node_at_front= Node(new_data1)

        # insertion can be done :
        # at the front of the linked list, 
        node_at_front.next = self.head
        self.head= node_at_front
         # after a given node, 
    def insertAfter(self, previousNode, new_data2):
        # first check if the previous node exists in the linked list
        node_between = Node(new_data2)
        if previousNode is None:
            print("The given node doesnot exixts int he linked list.")
        node_between.next = previousNode.next
        previousNode.next = node_between

        # at the end of the linked list
    def insertEnd(self, new_data3):
        node_at_end = Node(new_data3)
        # check if the linked list is empty, in that case make new node the head
        if self.head is None:
            self.head = node_at_end         
            return
        # else traverse to the last exisiting node
        last = self.head
        while(last.next):
            last = last.next
        # change the next of the last node to the new node
        last.next = node_at_end
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
      

llist= LinkedList()
llist.head= Node(1)
second= Node(2)
third= Node(3)
llist.head.next= second
second.next= third 
llist.push(0)
llist.insertAfter(second, 2.5)
llist.insertEnd(4)
llist.printList()
        


