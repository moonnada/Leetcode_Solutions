# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        '''
        M: bfs
            
        p: 
            1. init a que, maxSum, maxLevel
            2. while que:
                2.1) level ++, init the curSum 
                2.2) looping cur level to get curSum
                    2.3) put each side into queue
                2.4) compare cursum and level to get max
        '''
        
        maxSum = float('-inf')
        maxLevel = curLevel = 0
        que = deque([root])
        
        while que:
            curLevel += 1
            curSum = 0
            
            for _ in range(len(que)):
                curNode = que.popleft()
                curSum += curNode.val
                
                if curNode.left:
                    que.append(curNode.left)
                    
                if curNode.right:
                    que.append(curNode.right)
                    
            
            if maxSum < curSum:
                maxSum = curSum
                maxLevel = curLevel
                
        return maxLevel