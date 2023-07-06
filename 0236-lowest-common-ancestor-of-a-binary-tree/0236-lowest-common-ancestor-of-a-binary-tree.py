# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        M: DFS
        
        P: 
            1. check edge cases(null, root.val is equal to p or q)
            2. visit both sides recursively
            3. if both side exist, then return root
            4. return one of node which exists
        
        '''
        
        if not root or root == p or root == q: return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p,q)
        
        if left and right: return root
        
        return left or right