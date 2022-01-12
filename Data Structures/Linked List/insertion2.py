class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head =None
    def printLinkedList(self):
        temp = self.head
        while(temp):
            print(temp.head)
            temp = temp.next

    def push(self, frontData):
        frontNode= Node(frontData)
        # to insert at the front, first create the new node, point the new node's next to the current head, 
        # then assign the head to the new node
        frontNode.next = self.head
        self.head= frontNode

    def insertAfter(self, previousNode, afterData):
        afterNode = Node(afterData)
        # to insert a node after a previous node, first check if the previous node exists in the linked list
        if previousNode is None:
            print("The give node doesnot exists in the linked list.")
        # then assign previous node's next to the new node's next
        afterNode.next= previousNode.next
        # now point previous node's next to the new node
        previousNode.next = afterNode
    
    def append(self, endData):
        endNode= Node(endData)
        # to insert a node at the end, first check if the list is empty or not
        if self.head is None:
            self.head= endNode
            return
        # if not, traverse through the list to find the last node
        last = self.head # start from the head
        while(last):
            last =last.next
        # once we get the last node, simply assign the current last node's next tot eh new node
        last.next = endNode


llist = LinkedList()
llist.head= Node(1)
second = Node(2)
third =Node(3)

        
        