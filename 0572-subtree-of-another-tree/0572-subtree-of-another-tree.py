# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False
        
        def sameTree(root, subRoot):
            if not root and not subRoot: 
                return True
            
            if root and subRoot:
                return root.val == subRoot.val and sameTree(root.left, subRoot.left) and sameTree(root.right, subRoot.right)
            
        if sameTree(root, subRoot): return True
    
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
        
            
        