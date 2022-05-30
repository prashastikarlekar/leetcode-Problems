class Node:
    def __init__(self,data):
        self.data =data
        self.next = next
class LinkedList:
    def __init__(self) :
        self.head = None
    def hasCycle(self):
        setOfNodes= set()
        while self.head is not None:
            if self.head in setOfNodes:
                print(True)
            setOfNodes.add(self.head)
            self.head = self.head.next


            

        


