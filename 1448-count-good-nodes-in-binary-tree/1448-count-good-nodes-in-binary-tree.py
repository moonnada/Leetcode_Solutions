# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        ans = 0
        
        def helper(node, maxVal):
            nonlocal ans
            
            if node.val >= maxVal:
                ans += 1
                
            if node.left: helper(node.left, max(maxVal, node.val) )
            if node.right: helper(node.right, max(maxVal, node.val))
            
        helper(root, float(-inf))
        
        return ans
        
        
#         bfs. time: o(n), space: o(n)
#         if not root: return 0
#         que = [[root, float(-inf)]]
#         good = 0
        
#         while que:
#             [curNode, maxVal] = que.pop(0)
            
#             if curNode.val >= maxVal:
#                 maxVal = curNode.val
#                 good += 1
                
#             if curNode.left:
#                 que.append([curNode.left, maxVal])
            
#             if curNode.right:
#                 que.append([curNode.right, maxVal])
                
#         return good
        