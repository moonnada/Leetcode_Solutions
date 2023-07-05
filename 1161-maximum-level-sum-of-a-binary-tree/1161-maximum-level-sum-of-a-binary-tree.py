# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        '''
        U:
            ex)
                    4
                    /\
                   2  5
                   / 
                  2 
                  /
                  3
        M: BFS (queue)
        
        P:
            1. init a val for maxSum and curSum
            2. init a queue
            3. while que exist
                3.1) pop cur node from queue
                3.2) looping check children of cur node
                3.3) get curSum and add each node into queue
                3.4) calculate maxSum
            
        '''
        
#         maxSum = float('-inf')
#         curSum = 0
#         curLevel = 0
#         maxLevel = 0
#         que = deque([root])
        
#         while que:
#             curLevel += 1
            
#             for _ in range(len(que)):
#                 curNode = que.popleft()
#                 curSum += curNode.val
                
#                 if curNode.left:
#                     que.append(curNode.left)
                    
#                 if curNode.right:
#                     que.append(curNode.right)
                    
#             if maxSum < curSum:
#                 maxSum = curSum
#                 maxLevel = curLevel
                
#         return maxLevel
        if not root: return 0
        max_sum = float("-inf")
        max_level = 0
        current_level = 0

        q = deque([root])
        
        while q:
            current_level += 1
            current_level_sum = 0
    
            for _ in range(len(q)):
                current_node = q.popleft()
                current_level_sum += current_node.val

                if current_node.left: q.append(current_node.left)
                if current_node.right: q.append(current_node.right)

            if current_level_sum > max_sum:
                max_sum = current_level_sum
                max_level = current_level
            
        return  max_level