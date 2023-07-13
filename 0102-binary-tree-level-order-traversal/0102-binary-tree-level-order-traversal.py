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
            
            
        M: DFS
        
        P:
            1. check edge case(null)
            2. init an ans list and level value
            3. init a helper fuc
                3.1) if len of list == level, start a new []
                3.2) put cur node val into list
                3.3) if curnode.left exists, visit there
                3.4) if curnode.right exists, visit there
        '''

        if not root: return []
        
        levels = []
        
        def helper(node, level):
            if len(levels) == level: 
                 levels.append([])

            levels[level].append(node.val)
            
            if node.left:
                helper(node.left, level+1)
                
            if node.right:
                helper(node.right, level+1)
                
        helper(root, 0)
        
        return levels
        
        