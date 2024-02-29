# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = [[p,q]]
        
        while queue:
            curP, curQ = queue.pop(0)
            
            if curP and curQ and curP.val == curQ.val:
                queue.append([curP.left , curQ.left])
                queue.append([curP.right, curQ.right])
            elif curP is not curQ:
                return False
        return True
                
        
#         if not p and not q:
#             return True
        
#         if not p or not q:
#             return False
        
#         return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            