# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2) -> ListNode:
        
        engine =ListNode(-1) # create a fake node, output stores this node's address, pointing towards first node
        lastDabba = engine # this variable stores reference of output, outputlist is pointing tot ht elist node, whatever is in output is in outputList, outputlist is pointing towards the last added node 
        while(l1 and l2):              
            if l1.val <= l2.val:
                lastDabba.next= l1
                l1 = l1.next
            else:
                lastDabba.next = l2
                l2 = l2.next
            lastDabba = lastDabba.next
            
        lastDabba.next = l1 if l1 is not None else l2
        return engine.next
print(mergeTwoLists())