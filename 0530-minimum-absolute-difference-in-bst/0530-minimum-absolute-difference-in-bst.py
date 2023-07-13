# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        '''
        U:
            key point:
                need to visit every node and get differences
                
            q) input tree can be empty?
            
        M: In order
        
        P:
            1. check edge case(null)
            2. init a min and prev
            3. make a helper func to visit node in the inorder way
                3.1) if node is null, retuen null
                3.2) visit the left child
                3.3) if prev val exists, get min val 
                3.4) visit the right child
            4. run the helper func
                        
            
        Time: o(n), space: o(n)
        '''
        
#         self.prev = None
#         self.minVal = 1e9
        
#         def inorder(node):
#             if not node: return
            
#             inorder(node.left)
#             if self.prev:
#                 self.minVal = min(self.minVal, node.val - self.prev)
            
#             self.prev = node.val
#             inorder(node.right)
            
#         inorder(root)
        
#         return self.minVal
        self.minDistance = 1e9
        # Initially, it will be null.
        self.prevNode = None

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            # Find the difference with the previous value if it is there.
            if self.prevNode is not None:
                self.minDistance = min(self.minDistance, node.val - self.prevNode)
            self.prevNode = node.val
            inorder(node.right)

        inorder(root)
        return self.minDistance
        
        
    