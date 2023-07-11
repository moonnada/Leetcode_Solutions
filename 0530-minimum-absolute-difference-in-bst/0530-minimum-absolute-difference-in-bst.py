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
            2. init a min val
            3. visit both sides recursively
            4. get a min val
        '''
        
        if not root: return 
        nodeList = []
        minVal = 1e9
        
        def inorder(root):
            if not root: return
            
            inorder(root.left)
            nodeList.append(root.val)
            inorder(root.right)
            
        inorder(root)
        
        for i in range(1, len(nodeList)):
            minVal = min(nodeList[i]-nodeList[i-1], minVal)
            
        return minVal
        
    