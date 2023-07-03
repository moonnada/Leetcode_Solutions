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
        '''
        
        '''
            #DFS
            1. check edge cases(null, one node)
            2. check cur values
            3. recursion both sides
        '''
#         if not p and not q: return True
        
#         if not p or not q: return False
        
#         if p.val != q.val: return False
        
#         return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)

        '''
            #BFS
            1. check edge cases(null, one node)
            2. init a queue for both trees
            3. while queue exists
                3.1) pop a val from each queue
                3.2) compare the values. if there are same, put each side's val into queue
                3.3) if p and q are different nodes, then false
            4. true
        '''
        
        # if p and q: return True
        # if not p or not q: return False
        # if p.val != q.val: return False
    
        que = deque([(p,q)])
        while que:
            p,q = que.popleft()
            if p and q and p.val == q.val:
                que.append((p.left, q.left))
                que.append((p.right, q.right))
            
            elif p is not q:
                return False
        
        return True