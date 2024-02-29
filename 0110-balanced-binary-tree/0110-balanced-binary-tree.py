# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root: return True
        
        queue = [root]
        leftHeight, rightHeight = 0,0
        
        def getHeight(node):
            if not node:
                return 0
            return 1 + max(getHeight(node.left), getHeight(node.right))
        
        while queue:
            for i in range(len(queue)):
                curNode = queue.pop(0)
                leftHeight = getHeight(curNode.left)
                rightHeight = getHeight(curNode.right)
                
                if abs(leftHeight - rightHeight) > 1:
                    return False
                
                if curNode.left:
                    queue.append(curNode.left)
                    
                if curNode.right:
                    queue.append(curNode.right)
                    
        return True
                
                
        '''
        unbalanced ? height difference > 1
        dfs
        
        1. check edge case
        2. init a height as 0
        3. make a helper func to track height
            3.1) in a helper func, first check if node not exist, return
            3.2) left = node.left , right = node.right
            3.3) if abs(left - right) > 1: return false, else true
            
            
        
        '''
#         if not root: return True
        
#         def getHeight(node):
#             if not node: return -1
            
#             return 1 + max(getHeight(node.left) , getHeight(node.right))
        
#         return abs(getHeight(root.left) - getHeight(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)