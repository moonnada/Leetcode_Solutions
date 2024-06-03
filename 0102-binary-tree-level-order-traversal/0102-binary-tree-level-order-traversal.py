# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        que = [root]
        ans = []
        
        while que:
            curLevel = []
            for i in range(len(que)):
                curNode = que.pop(0)
                
                if curNode.left:
                    que.append(curNode.left)
                    
                if curNode.right:
                    que.append(curNode.right)
                    
                curLevel.append(curNode.val)
            
            ans.append(curLevel)
            
        return ans
        
        