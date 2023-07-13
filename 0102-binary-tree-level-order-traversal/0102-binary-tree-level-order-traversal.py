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
            3. put curNode.val into list
            4. ans.append([])
            5. visit curnode.left and put the val into list
            6. visit curnode.right and put the val into list
        '''
      
        levels = []
        if not root: return []
        
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