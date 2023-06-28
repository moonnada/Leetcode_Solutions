# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        '''
        U:
            q) what if list is empty? can I use the same number multiple times? input list is sorted?
            
            ex) P1              P2
                1 - 2 - 4 - 3 - 5
            
            =>  1 - 5 - 2 - 3 - 4
            
        P:
            1. check edge cases (empty, one node)
            2. find middle
            3. reverse the second half
            4. merge two halfs
            
        time: o(n), space: o(1)
        '''
        
        if not head or not head.next: return head
        
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        
        second = slow.next
        prev = slow.next = None
        
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
            
        first = head
        second = prev
        
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            
            first = tmp1
            second = tmp2
        