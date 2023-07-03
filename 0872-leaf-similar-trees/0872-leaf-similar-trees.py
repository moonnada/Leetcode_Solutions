# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        '''
        M: recursion(dfs)
        
        P:
            1. make a func for recursion
                1.1) if root not exist, return empty list
                1.2) if root doesnt have one of sides, then put cur val into list
                1.3) root has both a left and a right child, so the dfs func is called recursively and combine the result and return the val
            2. check root1 and root2 lists are same
            
        '''
        return self.dfs(root1) == self.dfs(root2)
     
    def dfs(self, root):
        if not root: return []
        if not (root.left or root.right): return [root.val]
        return self.dfs(root.left) + self.dfs(root.right)
        
