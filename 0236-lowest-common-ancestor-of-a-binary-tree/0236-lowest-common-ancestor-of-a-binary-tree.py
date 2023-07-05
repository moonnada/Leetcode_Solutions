# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        M: DFS (recursion)
        
        P: 
            1. check edge cases(null, one node)
            2. visit both sides recursively
            3. if both sides exist, then just retun root
            4. return one of side when exists
        '''
        #time: o(n), space: o(1) if not countring recursive, otherwise o(n)
        
        if not root or root == p or root == q: return root
        
        leftVal = self.lowestCommonAncestor(root.left, p,q)
        rightVal = self.lowestCommonAncestor(root.right, p,q)
        
        if leftVal and rightVal:
            return root
        
        return leftVal or rightVal

       

        