# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        U:
        
            ex) 1 -> 2 -> 3 -> 4 -> 5
            p  c,n
            
            p 
        '''
        
        if not head or not head.next: return head
        
        cur = head
        prev = None
        nxt = None
        
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            
        return prev