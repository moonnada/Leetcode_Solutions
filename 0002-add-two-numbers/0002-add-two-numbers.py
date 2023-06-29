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
                ex) l1 = [1,4,5,2], l2 = [2,9]
                
                1452
                29
                3362
                
            P:
                1. check egde cases(one node)
                2. while both lists exist, add each node. if both sum > 9, then put 0 and add 1 to the next position
                3. if one of list doesnt exist anymore, just put into the new list
                4. reverse the new list
                
        '''
        
            
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            carry, out = divmod(val1 + val2 + carry, 10)
                
            curr.next = ListNode(out)
            curr= curr.next
                
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
                
        return dummy.next