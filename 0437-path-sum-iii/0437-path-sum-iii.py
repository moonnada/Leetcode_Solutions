# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        '''
        U:
            
        M: dfs
        '''
        self.cnt = 0
        self.lookup = defaultdict(int)
        self.lookup[targetSum] = 1
        
        def dfs(node, rootSum):
            if not node: return
            
            rootSum += node.val
            self.cnt += self.lookup[rootSum]
            self.lookup[rootSum + targetSum] += 1
            dfs(node.left, rootSum)
            dfs(node.right, rootSum)
            
            self.lookup[rootSum + targetSum] -= 1
            
        dfs(root, 0)
        
        return self.cnt