# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        U:
            q) if input tree has no child, then return 0?
            
        M: DFS
        
        P:
            1. check edge case(one child)
            2. make a helper fuc to calculate length
                2.1) if not root: return 0
                2.2) return 1 + max( root.left , root.right)
        '''
        
        def dfs(root):
            nonlocal diameter
            if not root: return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            diameter = max(diameter, left + right)
            return max(left, right) + 1
        
        diameter = 0
        dfs(root)
        
        return diameter
            
        