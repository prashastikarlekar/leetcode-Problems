class Node:
    def __init__(self,data):
        self.data =data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def addLast(self,data):
        newNode = Node(data)
        temp= self.head
        while(temp):
            if temp.next == None:
                temp.next = newNode
            temp = temp.next
        
    def getSize(self):
        temp= self.head
        size =0
        while(temp):
            size+=1
            temp=temp.next
        return size

    def printElements(self):
        temp  = self.head
        while(temp):
            print(temp.data)
            temp =temp.next

    def removeFirst(self):
        temp = self.head
        self.head = temp.next
    
    def getfirst(self):       
        if self.head ==None:
            return "The list is empty."
        else:
            return self.head.data
    
    def getLast(self):
        temp = self.head
        while(temp):
            if temp.next == None:
                return temp.data
            temp = temp.next

    def getAt(self,index):
        if index ==0:
            return self.getfirst()
        elif self.getSize() == index-1:
            return self.getLast()
        else:
            temp = self.head
            for i in range(index):
                temp = temp.next
            return temp.data

    def addFirst(self,data):
        newNode = Node(data)
        newNode.next= self.head
        self.head = newNode
    
    def addAt(self,index,data):
        newNode= Node(data)
        if index ==0:
            return self.addFirst(data)
        i=0
        temp =self.head
        while(i<index-1):

            temp =temp.next
            i+=1
        newNode.next = temp.next
        temp.next = newNode
    
    def removeLast(self):
        temp = self.head
        prev=None
        while(temp.next != None):
            prev =temp
            temp = temp.next
        prev.next = None
    def removeAt(self,index):
        prev=None
        current = self.head
        
        while(index-1):
            prev= current
            current = current.next
            index-=1
        prev.next = current.next
        return self.head


        