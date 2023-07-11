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
            
        M: DFS (recursion)
        
        P:
            1. check edge case(null)
            2. init a min val
            3. visit both sides recursively
            4. get a min val
        '''
        
        if not root: return -1
        
        minVal = 99999999
        self.nodeList = []
        
        self.inorder(root)
        for i in range(1, len(self.nodeList)):
            minVal = min(abs(self.nodeList[i] - self.nodeList[i-1]), minVal )
        
        return minVal
    
    def inorder(self, root):
        if not root: return
        
        self.inorder(root.left)
        self.nodeList.append(root.val)
        self.inorder(root.right)
        
    