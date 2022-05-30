# code to imlement motus  give n question on linkdxlist
class Box: # class to construct a box node
    def __init__(self, size) :
        self.size =size
        self.next = None

# class LinkedList: # class to contruct linked list of boxes
#     def __init__(self) :
#         self.head = None
#     def printAllElements(self):
#         temp = self.head
#         while(temp):
#             print(temp.size)
#             temp = temp.next

if __name__=="__main__":
    # create first linked list box1
    # box1 = LinkedList()
    # create nodes for the first linked list
    firstBox1= Box(2)
    secondBox1 = Box(5)
    thirdBox1= Box(12)
    forthBox1 = Box(18)
    fifthBox1 = Box(27)
    # link the nodes together
    # box1.head = firstBox1
    box1 = firstBox1

    firstBox1.next  =secondBox1
    secondBox1.next = thirdBox1
    thirdBox1.next = forthBox1
    forthBox1.next = fifthBox1


    # create second linked list
    # box2 = LinkedList()
    # create nodes for the second linked list

    firstBox2 = Box(4)
    secondBox2 = Box(15)
    thirdBox2 = Box(42)
    forthBox2 = Box(53)
    fifthBox2 = Box(100)
    # link the nodes together
    box2 =firstBox2

    firstBox2.next = secondBox2
    secondBox2.next = thirdBox2
    thirdBox2.next = forthBox2
    forthBox2.next = fifthBox2

    # box1.printAllElements()
    # box2.printAllElements()

    # firstly, create the engine 

    engine = Box(0)
    # add the boxes to the engine

    current= engine
    while(box1 and box2):
        if box1.size <= box2.size:
            current.next = box1 
            box1= box1.next
        else:
            current.next = box2
            box2= box2.next
        current = current.next
    
    current.next = box1 if box2==None else box2

    firstNode = engine.next
    while(firstNode!=None):
        print(firstNode.size)
        firstNode = firstNode.next
    # print(engine.next)

        