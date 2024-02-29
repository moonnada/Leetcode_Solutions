# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        que = [root]
        dep = 0
        
        
        
        while que:
            for i in range(len(que)):
                curNode = que.pop(0)
                
                if curNode.left:
                    que.append(curNode.left)
                if curNode.right:
                    que.append(curNode.right)
                
            dep += 1
            
        return dep
            
            
#         if not root: return 0
        
#         maxDep = 1
        
#         left = self.maxDepth(root.left)
#         right = self.maxDepth(root.right)
        
#         return max(left, right) + 1
        
