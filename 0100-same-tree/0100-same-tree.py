# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        U:
            q) input tree can be null?
            
        M: binary
            1. recursion (DFS)
        
        P: 
            1. check edge cases(null, one node)
            2. check cur values
            3. recursion both sides
            
        '''
#         if not p and not q: return True
        
#         if not p or not q: return False
        
#         if p.val != q.val: return False
        
#         return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)

        que = deque([(p,q)])
        while que:
            p, q = que.popleft()
            if p and q and p.val == q.val:
                que.append((p.left, q.left))
                que.append((p.right, q.right))
                
            elif p is not q:
                return False
        return True