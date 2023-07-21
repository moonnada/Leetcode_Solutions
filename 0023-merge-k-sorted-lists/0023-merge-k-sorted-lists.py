# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        node = []
        head = ptr = ListNode(0)
        for i in lists:
            while i:
                node.append(i.val)
                i = i.next
                
        for i in sorted(node):
            ptr.next = ListNode(i)
            ptr = ptr.next
            
        return head.next