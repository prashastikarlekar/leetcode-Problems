# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        
        if(head==None): return None
        my_stack = []
        current=head
        
        while(current!=None):
            my_stack.append(current)
            current=current.next
        
        head.next = None
        
        new_head = my_stack.pop()
        current = new_head
        while(len(my_stack)!=0):
            current.next = my_stack.pop()
            current = current.next
        
        return new_head
        
        