# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        que = [[p,q]]
        
        while que:
            curP, curQ = que.pop(0)
            if curP and curQ and curP.val == curQ.val:
                que.append([curP.left, curQ.left])
                que.append([curP.right, curQ.right])
            
            elif curP != curQ:
                return False
        return True
#         dfs. time:o(n), space: o(n)
#         if not p and not q: return True
#         elif not p or not q or p.val != q.val: return False
        
#         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
              
    