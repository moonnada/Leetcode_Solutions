# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        U:
            check bst
            q) input root can be empty
            q) tree can have the same number?
            
        M: bfs
        
        P:
            1. check edge case(null)
            2. init a que
            3. while queue exists
                3.1) pop curNode from queue
                3.2) if curNode.left exists and the val is less than root, put the val into queue
                3.3) if curNode.right exists and the val is greater than root, put the val into queue
                3.4) else return false
            4. return true 
            
        time: o(n), space: o(n)
                    
        '''
        
        que = deque()
        que.append((root, float('-inf'), float('inf') ))
        
        while que:
            node, minVal, maxVal = que.popleft()
            
            if node:
                if minVal >= node.val or node.val >= maxVal: return False
                
                if node.left: 
                    que.append((node.left, minVal, node.val))
                    
                if node.right:
                    que.append((node.right, node.val, maxVal))
                    
        return True
            