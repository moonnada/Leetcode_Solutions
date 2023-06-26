# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        U: 
            ex) 1 -> 3 -> 5 -> 9
            
            => 1 -> 3 -> 9
            
        M : linked list
        
        P:
            1. check edge cases(empty, one node)
            2. traverse the input list to count node
            3. get a mid point. if cnt of node is even, cnt/2 + 1. if not cnt / 2
            4. init node points (cur..)
            5. while cur:
                5.1) if curIndex is on the mid point, then skip the curIndex
                5.2) else keep moving forward
        
        '''
        
        if not head or not head.next: return None
        
        slow = head
        fast = head.next.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        slow.next = slow.next.next
        
        return head
        
        
      