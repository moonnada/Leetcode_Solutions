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
            2. make a helper func to visit nodes recursively
                2.1) check curnodes values of both trees are equal
                2.2) 
        
        '''
        
        if not root: return False
        
        if self.isSameTree(root, subRoot): return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, root, subRoot):
        if root and subRoot:
            return root.val == subRoot.val and self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)
            
        return root is subRoot