# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        '''
        def path(root, targetSum):
            if not root: return 0
            res = 0
            
            if root.val == targetSum: res += 1
            
            res += path(root.left, targetSum - root.val)
            
            res += path(root.right, targetSum - root.val)
            
            return res
        
        if not root: return 0
        
        return self.pathSum(root.left, targetSum) + path(root, targetSum) + self.pathSum(root.right, targetSum)
        '''
        
        def dfs(node, curr):
            if not node: return
            
            nonlocal ans, mark
            
            curr += node.val
            ans += mark[curr]
            
            goal = curr + targetSum
            mark[goal] += 1
            dfs(node.left, curr)
            dfs(node.right, curr)
            mark[goal] -= 1
        
        ans = 0
        mark = defaultdict(int)
        mark[targetSum] = 1
        dfs(root, 0)
        return ans