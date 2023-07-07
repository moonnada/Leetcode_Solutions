# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        U:
            q) what if both trees are none?
            
        M: dfS
        
        P:
            1. check edge cases(null..)
            2. check cur trees are same by using a helper func
            3. keep comparing both sides of root with subroot 
            4. in a helper func, 
                4.1) check both trees are none. if it is, return true
                4.2) keep comparing both sides of node and values
        
        '''
        
        if not root: return False
        
        if self.isSameTree(root, subRoot): return True
        
        return self.isSubtree(root.left , subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, root, subRoot):
        if not root and not subRoot: return True
        if root and subRoot:
            return root.val == subRoot.val and self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)
        