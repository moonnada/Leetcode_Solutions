# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        U:
            key points: 
                1. not bst
                2. good node : in the path from root to cur node that are no nodes with a val greater than curnode   
            q) input tree can be empty?
            
        M: DFS
        
        P:
            1. check edge case(null) and init a count val
            2. make a helper func to compare between child's vals and parents val
                2.1) if not root, return 
                2.2) if root.left exists, visit there and compare values. if it is a good node, cnt++
                2.3) if root.right exists, visit there and compare values. if it is a good node, cnt++
            3. return cnt
        '''
        if not root: return 0
        cnt = 0
        
        def dfs(node, maxVal):
            nonlocal cnt
            if node.val >= maxVal: cnt+=1
                
            if node.left:
                dfs(node.left, max(maxVal, node.val))
                
            if node.right:
                dfs(node.right, max(maxVal, node.val))
        
        dfs(root, float('-inf'))
        
        return cnt
        