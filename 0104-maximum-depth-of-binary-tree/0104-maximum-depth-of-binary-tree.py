# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        maxDep = 1
        
        def depth(node):
            if not node: return 0
            
            getLeft = depth(node.left)
            getRight = depth(node.right)
               
                
            return max(getLeft, getRight) + 1
        
        return depth(root)
        