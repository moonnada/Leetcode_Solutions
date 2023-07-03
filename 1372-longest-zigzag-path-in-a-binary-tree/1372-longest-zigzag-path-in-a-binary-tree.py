# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        '''
        U:
            key point
            1. need to remember what the recent direction was
            
        M: DFS , recursion
        
        P:
            1. check edge cases( null , one node)
            2. return max of both sides of root
            3. make a helper func to visit recursively
                3.1) check cur root exists. if not, return cur depth
                3.2) if cur direction is left, visit alternatively add depth + 1. AND THEN visit current direction with 0 depth
                3.3) else, visit alternatively add depth + 1. AND THEN visit current direction with 0 depth
                3.4 return depth    
        '''
      
        if not root: return 0
        if not root.left and not root.right: return 0
        
        return max( self.dfs(root.left, True, 0), self.dfs(root.right, False, 0))
    
    def dfs(self, root, isLeft, depth):
        if not root: return depth
        
        if isLeft:
            depth = max(
                depth,
                self.dfs(root.right, False, depth+1),
                self.dfs(root.left, True, 0)
            )
        else:
            depth = max(
                depth,
                self.dfs(root.left, True, depth+1),
                self.dfs(root.right, False, 0)
            )
        
        return depth