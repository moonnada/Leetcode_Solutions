# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        que = [[root,0]]
        ans = []
        
        while que:
            [curNode, level] = que.pop(0)
            if len(ans) == level: ans.append(curNode.val)
            
            if curNode.right: que.append([curNode.right, level+1])
            if curNode.left: que.append([curNode.left, level+1])
                
        return ans