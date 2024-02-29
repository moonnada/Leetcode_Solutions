# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        que = [root]
        
        while que:
            curNode = que.pop(0)
            curNode.left , curNode.right = curNode.right , curNode.left
            
            if curNode.left:
                que.append(curNode.left)
            if curNode.right:
                que.append(curNode.right)
        
        return root
        
#         if not root:
#             return root
        
#         left = self.invertTree(root.left)
#         right = self.invertTree(root.right)
               
#         root.left = right
#         root.right = left
        
#         return root