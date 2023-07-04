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
            q) root can be null?
            q) can root have the same numbers multiple times?
            
        M: DFS (recursion)
        
        P: 
            1. check edge cases( null, one node)
            2. visit each side recursively
            3. invert each side
            4. return root
        '''
        
        if not root: return None
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        
        root.left = right
        root.right = left
        
        return root
        