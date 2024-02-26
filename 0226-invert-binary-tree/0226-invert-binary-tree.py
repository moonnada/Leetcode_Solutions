# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         bfs
#         if not root: return root
        
#         left = self.invertTree(root.left)
#         right = self.invertTree(root.right)
        
#         root.left = right
#         root.right = left
        
    
#         return root

#       dfs
        if not root: return root
    
        queue = [root]
        
        while queue:
            curNode = queue.pop(0)
            
            curNode.left, curNode.right = curNode.right, curNode.left
            
            if curNode.left:
                queue.append(curNode.left)
                
            if curNode.right:
                queue.append(curNode.right)
          
                
         
                    
        return root