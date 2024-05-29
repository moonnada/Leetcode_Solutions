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
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return max(left, right) +1
        
#         time: o(n), space: o(1)
#         if not root: return 0
        
#         cur = 0
#         que = [root]
        
#         while que:
#             for i in range(len(que)):
#                 curNode = que.pop(0)

#                 if curNode.left:
#                     que.append(curNode.left)
#                 if curNode.right:
#                     que.append(curNode.right)
#             cur += 1

    
#         return cur
    
        