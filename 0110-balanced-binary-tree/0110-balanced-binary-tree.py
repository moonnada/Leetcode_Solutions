# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        que = [root]
        
        def getHeight(node):
            if not node: return 0
            
            return 1+ max(getHeight(node.left), getHeight(node.right))
        
        while que:
            curNode = que.pop(0)
            left = getHeight(curNode.left)
            right = getHeight(curNode.right)
            
            if abs(left-right) > 1: 
                return False
            
            if curNode.left:
                que.append(curNode.left)
                
            if curNode.right:
                que.append(curNode.right)
                
        return True
            
        
        
#         if not root: return True
        
#         def helper(node):
#             if not node: return 0
            
#             return 1 + max(helper(node.left), helper(node.right))
        
#         return abs(helper(root.left) - helper(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)