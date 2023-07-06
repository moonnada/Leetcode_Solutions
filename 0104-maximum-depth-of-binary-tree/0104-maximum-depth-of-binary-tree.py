# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        U:
            ex) root can be empty?
            ex) the input tree is considered as a bst?
            
        M: BST
        
        P: 
            1. check edge case (null)
            2. init a que and detph as 1
            3. while que
                3.1) curNode is popped from que
                3.2) if curnode.left, add the node into queue
                3.3) if curnode.right, add the node into queue
                3.4) depth++
            4. return depth
        '''
        
        if not root: return 0
        depth = 0
        que = deque([root])
        
        while que: 
            
            for _ in range(len(que)):
                curNode = que.popleft()


                if curNode.left:
                    que.append(curNode.left)
                    
                if curNode.right:
                    que.append(curNode.right)
            
            depth +=1
            
        return depth