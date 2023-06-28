# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        U:
            q) list can have negative or decimal num?
            
        P: 
            1. check edge cases(empty, one node)
            2. init a prev ptr and ptr for both list
            3. while each ptr.next exists
                3.1) compare cur ptr and make a connection between small ptr. and then the ptr moves to the next one 
            4. if one of list is null, then make a connection between the other list
            
        '''
        
        if not list1 and not list2: return None
        
        if not list1: return list2
        
        if not list2: return list1
        
        prehead = ListNode(-1)
        prev = prehead
        
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
                
            prev = prev.next
                
        prev.next = list1 if list1 is not None else list2
            
        return prehead.next