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
            
            c
               n
         M: linked list
         
         P: 
            1. check edge cases(empty, one len)
            2. make a prev node as a current node
            3. c = head.next
            4. c = head
            5. head = c.next
            
          
         
        '''
        if not head or not head.next : return head
        prev = None
        nxt = None
        curr = head
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev