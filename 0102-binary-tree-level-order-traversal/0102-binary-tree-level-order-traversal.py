# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        U:
            q) node val is only integer?
            
        M: BFS
        
        P:
            1. check edge case(null)
            2. init an ans list and queue
            3. while que exists
                3.1) pop cur node from queue
                3.2) visit cur level of node by using a loop    
                    3.3) put cur node into queue and list
            4. return list        
            
        '''
        if not root: return []
        que = deque([root])
        ans = []
        level = 0
        
        while que:
            ans.append([])
            
            for _ in range(len(que)):
                curNode = que.popleft()
                ans[level].append(curNode.val)
                
                if curNode.left:
                    que.append(curNode.left)
                if curNode.right:
                    que.append(curNode.right)
            level+=1
            
        return ans
                
        