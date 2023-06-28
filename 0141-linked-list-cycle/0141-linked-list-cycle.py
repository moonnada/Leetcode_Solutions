# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        U:
            q) list can be empty?
            q) list can have the same num multiple times?
            
        P:
            1. check edge cases( empty, one node)
            2. init slow and fast ptrs
            3. while fast and fast.next exist
                3.1) both ptrs keep moving
                3.2) if both ptrs are on the same position, return true
            4. false
        '''
        
        if not head or not head.next: return False
        
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast: return True
        return False
        