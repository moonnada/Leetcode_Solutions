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
            1. check edge case(empty)
            2. init a diameter as 0
            3. run a helper func
            4. in a helper func,
                4.1) check if root is null. if it is, return 0
                4.2) visit both sides recursively 
                4.3) update the diameter val
                4.4) return max val between left and right + 1
           
        '''
        def dfs(root):
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.diameter = max( self.diameter, left + right)
            return max(left, right) + 1
        
        if not root: return 0
        self.diameter = 0
        dfs(root)
        return self.diameter

        