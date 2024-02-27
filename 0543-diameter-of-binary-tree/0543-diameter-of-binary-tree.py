# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        dfs
        
        1. check edge case
        2. init a diameter val 
        3. init a helper func (node, level)
        4. in a helper func,   
            4.1) if not node, return 0
            4.2) if node.left exists, visit there level + 1
            4.3) right, level +1
        '''
        if not root: return 0
        
        maxDia = 0
        queue = [[root, 0]]
        
        def getHeight(node):
            if not node: return 0

            return 1 + max(getHeight(node.left), getHeight(node.right))
        
        while queue:
            curNode, curHeight = queue.pop(0)
            
            if not curNode: continue
                
            leftHeight = 0 if not curNode.left else getHeight(curNode.left)
            rightHeight = 0 if not curNode.right else getHeight(curNode.right)
            maxDia = max(leftHeight + rightHeight, maxDia)
            
            queue.append([curNode.left, leftHeight])
            queue.append([curNode.right, rightHeight])
            
        
        return maxDia
    
        
        
#         if not root: return 0
#         diameter = 0
        
#         def helper(node, level):
#             if not node: return 
            
#             if node.left:
#                 helper(node.left, level+1)
                
#             if node.right:
#                 helper(node.right, level+1)
                
#             return max(helper(node.left, level+1), helper(node.right, level+1))
        
#         return helper(root, diameter)

    
