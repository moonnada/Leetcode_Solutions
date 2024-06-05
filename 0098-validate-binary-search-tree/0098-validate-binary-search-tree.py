# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return False
        
        def helper(node, leftChild, rightChild ):
            if not node: return True
            
            elif node.val <= leftChild or node.val >= rightChild:
                return False
            
            else: return helper(node.left, leftChild, node.val) and helper(node.right, node.val, rightChild)
            
        
        return helper(root,float('-inf') ,float('inf') )
        