# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        U:
            q) what if there is no right val?
            
        M: BFS
        
        p: 
            1. check edge cases( null, one node, no right side)
            2. init a list for ans
            3. put cur node into the ans list
            4. visit the right child recursively
        '''
        
        # if not root or not (root.left and root.right) or not root.right: return root
        
        res = []
        que = deque([root])
        
        while que:
            rightSide = None
            qLen = len(que)
            
            for i in range(qLen):
                node = que.popleft()
                if node:
                    rightSide = node
                    que.append(node.left)
                    que.append(node.right)
            
            if rightSide:
                res.append(rightSide.val)
                
        return res
        