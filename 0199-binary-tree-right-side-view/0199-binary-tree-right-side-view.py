# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        ans = []
        
        def helper(node,level):
            if not node: return
            
            if len(ans) == level: ans.append(node.val)
            
            if node.right:
                helper(node.right, level+1)
            if node.left:
                helper(node.left, level+1)
                
        helper(root, 0)
        return ans
#         bfs. time: o(n), space: o(n)
#         if not root: return []
#         que = [[root, 0]]
#         ans = []
        
#         while que:
#             [curNode, level] = que.pop(0)
           
#             if curNode.right:
#                 que.append([curNode.right, level+1])
#             if curNode.left:
#                 que.append([curNode.left, level+1])
                
#             if len(ans) == level:
#                 ans.append(curNode.val)
                
#         return ans
