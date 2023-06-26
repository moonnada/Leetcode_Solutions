# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        U:
            q) input list can be empty?
            q) input list consists only positive integer?
            
        ex) 1 -> 2 -> 3 -> 4 -> 5
        
         p  1  2   
            h
            c
         
         M: linked list
         
         P: 
            1. check edge cases(empty, one len)
            2. make a prev node as a current node
            3. c = head.next
            4. c = head
            5. head = c.next
            
            prev, curr = None, head
        while curr:
            curr.next, 
            prev, 
            curr = prev, curr, curr.next
        return prev
         
        '''
        
        prev = None
        nxt = None
        curr = head
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev