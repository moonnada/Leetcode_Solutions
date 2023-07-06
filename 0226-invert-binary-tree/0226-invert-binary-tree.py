# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        U:
            q) tree can be null?
            q) tree can have the same number multiple times?
            
        M: DFS
        
        P:
            1. check edge cases(null, one node)
            2. visit both sides(left and right) recursively
            3. invert each side from root
            4. return root
        '''
        
        if not root: return root
        if not root.left and not root.right: return root
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        
        root.left = right
        root.right = left
        
        return root
        
        