# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        diameter = 0
        que = [root]
        
        def getHeight(node):
            if not node: return 0
            
            return 1 + max(getHeight(node.left), getHeight(node.right))
        
        while que:
            curNode = que.pop(0)
            left = getHeight(curNode.left)
            right = getHeight(curNode.right)
            
            if curNode.left:
                que.append(curNode.left)
            if curNode.right:
                que.append(curNode.right)
            
            diameter = max(left+right, diameter)
        
        return diameter
        
        
        #         time: o(n), space: o(1)
#         if not root: return 0
        
#         self.diameter = 0
        
#         def helper(node):
#             if not node: return 0
            
#             left = helper(node.left)
#             right = helper(node.right)
            
#             self.diameter = max(left + right, self.diameter)
            
#             return max(left, right)+1
        
#         helper(root)
#         return self.diameter