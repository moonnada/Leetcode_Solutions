# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        '''
        M: DFS , recursion
        
        1. need to remember what the recent direction was
        P:
            1. check edge cases( null , one node)
            2. make a helper func to visit recursively
                2.1) check there is a left on the left or right side. if not, return cur depth
                2.2) 
    
        '''
        if not root: return 0
        if not root.left and not root.right: return 0
        
        return max(self.dfs(root.left, True, 0), self.dfs(root.right, False, 0))
    
    def dfs(self, root, isLeft, depth):
        if not root: return depth
            
        if isLeft:
            depth = max( depth,
                         self.dfs(root.right, False, depth+1),
                        self.dfs(root.left, True, 0)
                          )
        else:
            depth = max( depth,
                           self.dfs(root.left, True, depth + 1),
                            self.dfs(root.right, False,0)
                           )
        return depth