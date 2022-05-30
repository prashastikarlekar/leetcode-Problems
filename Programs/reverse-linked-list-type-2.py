# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        
        if(head==None): return None
        
        prev = None
        next = head.next
        current = head
        while(current!=None):
            current.next = prev
            prev = current
            current = current.next
        return prev
        
    
        
        
        