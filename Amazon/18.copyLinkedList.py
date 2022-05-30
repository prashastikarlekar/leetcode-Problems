class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.random= None # index of the node this is pointing to

# def indices(head):
#     map={}
#     temp = head
#     i=0
#     while temp:
#         if temp not in map:
#             map[temp] = i
#             i+=1
#         temp =temp.next
#     return map

# def copyList(head):
    # if head is None:
    #     return
    # temp = head
    # current = Node(0)
    # newHead = current
    # while temp :
    #     current.next = Node(temp.val)
    #     # current.next.random = temp.random
    #     # current.next = temp.next
    #     temp = temp.next
    #     current = current.next
    # originalmap = indices(head)
    # newmap= indices(newHead.next)
    # temp = newHead.next

    # while temp:
    #     positionInOriginal = originalmap[temp]
    #     temp.random = newmap[positionInOriginal].random
    #     temp = temp.next

    # return newHead.next
    # there is no bitch bigger than me in front of me
    
def printAllNodes(head):
    if head is None:
        return 
    temp = head
    while temp:
        print(f"The value of the node is {temp.val} and the random pointer stored in the node is {temp.random}")
        temp = temp.next

def copyList(head):
    nodeKey = {}
    curr = head
    while curr:
        nodeKey[curr] = Node(curr.val)
        curr = curr.next  
    nodeKey[None] = None
    newHead = Node(-1)
    curr = newHead
    while curr and head:
        curr.next = nodeKey[head]
        nodeKey[head].random = nodeKey[head.random]
        curr = curr.next
        head = head.next
    return newHead.next
# sar fod le kutiya apna 

if __name__=="__main__":
    head = Node(7)
    second = Node(13)
    third= Node(11)
    forth=Node(10)
    fifth = Node(1)
    head.next = second
    second.next = third
    third.next = forth
    forth.next = fifth
    second.random = 0 # to first node
    third.random = 4 # to the last node # 5th
    forth.random = 2 # to third node 
    fifth.random = 0 # to first node
    printAllNodes(copyList(head))
    # print(indices(head))

# shubhangi mishra ko gandu har koi bolega idhar
# na kuch aata h is gandu ko na kabhi aaega
# is bhen ki lodi ki maa ki chut bhosdi ki maregi kutteki maut
# itna bura din aaeega ki bhosdi wali apna sada sa thobda bhi nai dikha paegi kisiko 
#  abhi bhi nai dikha sakti hai but iske dost isse nafrat karenge but bhushan daya hi khaega poore time ispe or isko 
# apne ghar rakhega poora semester
# is maa ki chut ko aukkatt dikhegi
# is bhosdi wali ki gand faegi mere naam se or mere saare friends ke naam se
# is gandu ko na kuch aata h na kabhi aaega 
# iski maa ki chut
# mar jaa na shuhangi mishra tereko koi miss bhi nai karega ulta sab khushi manaenge ki maa ki chut se
# se jaan chhuti hai
# is bhosdi wali ko sab raste pe betha kar peetenge



def copyList2(head):
    temp = head
    map = {}
    while temp:
        map[temp] = Node(temp.val)
        temp = temp.next
    newhead = Node(0)
    current = newhead
    while current and head:
        current.next = map[head]
        current.next.random = map[head.random]
        current = current.next
        head = head.next
    return newhead.next