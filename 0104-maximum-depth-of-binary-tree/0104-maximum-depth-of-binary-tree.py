# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
#   dfs      
#         if not root: return 0
        
#         if not root.right:
#             return 1 + self.maxDepth(root.left)
        
#         if not root.left:
#             return 1 + self.maxDepth(root.right)
        
#         else:
#             return 1+ max(self.maxDepth(root.left), self.maxDepth(root.right))


        if not root: return 0
        queue = [root]
        depth = 0
        
        while queue:
            for i in range(len(queue)):
                curNode = queue.pop(0)

                if curNode.left:
                    queue.append(curNode.left)

                if curNode.right:
                    queue.append(curNode.right)
                
            depth += 1
            
        return depth
                
        