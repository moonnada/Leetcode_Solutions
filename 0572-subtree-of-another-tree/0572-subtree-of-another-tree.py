# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        U:
            q) what if both trees are none?
            
        M: dfS
        
        P:
            1. check edge cases(null..)
            2. make a helper func to visit nodes recursively
                2.1) check curnodes values of both trees are equal
                2.2) 
        
        '''
        
        def helper(node):
            if not node: return False
            
            elif is_identical(node, subRoot):
                return True
            
            return helper(node.left) or helper(node.right)
        
        def is_identical(node1, node2):
            if not node1 or not node2:
                return node1 is None and node2 is None
            
            return (node1.val == node2.val and is_identical(node1.left, node2.left) and is_identical(node1.right, node2.right))
        
        return helper(root)