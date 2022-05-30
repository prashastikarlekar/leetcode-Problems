# Given the head of a singly linked list, reverse the list, and return the reversed list.

class Node:
    def __init__(self,data) -> None:
        self.data =data
        self.next = None

if __name__=="__main__":            
    firstNode = Node(1)
    secondNode =Node(2)
    thirdNode= Node(3)
    forthNode= Node(4)
    fifthNode =Node(5)
    llist = firstNode
    engine = Node(0)
    previous = engine
    # print(previous.data)
    while(llist):
        temp = previous.next
        if(llist.next is None): # get to the end node
            lastNode= llist # make the end node, head of the list
            lastNode.next = previous
            previous.next =None # empty the previous nodes next pointer
            lastNode = previous
            print(lastNode)

        else:
            previous = previous.next # keeping track of the previous node
            print(previous)
        llist = llist.next

    while(engine.next):
        print(llist)
        llist =llist.next


list =[1,2,3,4,5]
for i in range(len(list)):
    print(i)
    print(len(list) -(i+1))
    temp = len(list)-(i+1)
    list[i]= list[temp]
    print(f"i is {i} and temp is {len(list)-(i+1)}")
    
    # list[i],list[i-(len(list)-1)] = list[i-(len(list)-1)]
print(list)
