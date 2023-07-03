# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        U:
            q) input tree can be null?
            
        M: binary
            1. recursion
        
        P: 
            1. check edge cases(null, one node)
            2. while both
            
        '''
        if not p and not q: return True
        
        if not p or not q: return False
        
        if p.val != q.val: return False
        
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)