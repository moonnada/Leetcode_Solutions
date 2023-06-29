# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
            U: 
                key points: 
                    1. non-empty
                    2. non-negative
                    3. stored in reverse order
                    4. return the sum as a linked list
                ex) l1 = [2,4,3,9], l2 = [5,6,4]
                
                2439
                564
                7089
                
            P:
                1. init a dummy list and set curr on dummy list
                2. init a carry val
                3. while l1 or l2 or carry
                    3.1) init a val for checking each list exists. if not, put 0
                    3.2) get carry and sum
                    3.3) curr.next = remainder of the sum
                    3.4) cur = cur.next
                    3.5) check if each node has next node, then move. if not put none
                
        '''
        
            
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            carry, out = divmod(val1 + val2 + carry , 10)
            
            curr.next = ListNode(out)
            curr = curr.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next