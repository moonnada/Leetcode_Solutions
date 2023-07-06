# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        U:
            q) tree can be null?
            q) tree can have the same number multiple times?
            
        M: DFS
        
        P:
            1. check edge cases(null, one node)
            2. visit both sides(left and right) recursively
            3. invert each side from root
            4. return root
        '''
        
#         if not root: return root
#         if not root.left and not root.right: return root
        
#         left = self.invertTree(root.left)
#         right = self.invertTree(root.right)
        
#         root.left = right
#         root.right = left
        
#         return root
        
        '''
        M: BFS (queue)
        
        P: 
            1. check edge case(null)
            2. init a queue
            3. while queue exists
                3.1) curnode is popped from queue
                3.2) if curNode.left , append curNode.right
                3.3) if curNode.right, append curnode.left
        '''
        
        if not root: return root
        que = deque([root])
        
        while que:
            curNode = que.popleft()
            curNode.left, curNode.right = curNode.right, curNode.left
            if curNode.left:
                que.append(curNode.left)
            
            if curNode.right:
                que.append(curNode.right)
                
        return root
            
        
        