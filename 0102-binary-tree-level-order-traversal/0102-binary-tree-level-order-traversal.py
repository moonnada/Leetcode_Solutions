# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         BFS
#         if not root: return []
#         queue = [root]
#         ans = []
        
#         while queue:
#             curLevel = []
            
#             for i in range(len(queue)):
#                 curNode = queue.pop(0)
                
#                 if curNode.left:
#                     queue.append(curNode.left)
                
#                 if curNode.right:
#                     queue.append(curNode.right)
                    
#                 curLevel.append(curNode.val)
                
#             ans.append(curLevel)
            
#         return ans
        
    
#         DFS
        if not root: return []
        
        ans = []
        
        def helper(node, level):
            if not node: return

            if len(ans) == level:
                ans.append([])
                
            ans[level].append(node.val)
            
            if node.left:
                helper(node.left, level+1)
                
            if node.right:
                helper(node.right, level+1)
        
        helper(root, 0)

        return ans
    