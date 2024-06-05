# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        
        que = [[root, float(-inf)]]
        ans = 0
        
        while que:
            [curNode, maxVal] = que.pop(0)
            
            if curNode.val >= maxVal:
                maxVal = curNode.val
                ans += 1
                
            if curNode.left:
                que.append([curNode.left, maxVal])
            if curNode.right:
                que.append([curNode.right, maxVal])
        
        return ans