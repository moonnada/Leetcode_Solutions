# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = [root]
        ans = []
        
        while queue:
            curLevel = []
            curQue = len(queue)
            
            for i in range(curQue):
                curNode = queue.pop(0)
                
                if curNode.left:
                    queue.append(curNode.left)
                    
                if curNode.right:
                    queue.append(curNode.right)
                    
                curLevel.append(curNode.val)
            
            ans.append(curLevel)

        return ans