# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        U:
            q) what if there is no right val?
            
        M: BFS
        
        p: (bfs)  
            1. init a list for answer
            2. init a queue with the root node
            3. while queue exists
                3.1) init a val to store the right side
                3.2) get a length of cur level of queue
                3.3) loop through the nodes in the cur level
                    3.4) dequeue the next node from the queue
                    3.5) if the node exists
                        3.6) update the rightside val to store the cur node
                        3.7) enqueue left and right side of the cur node
                3.8) after processing all nodes in the cur level, if rightside is not null, then add the cur val to the ans list
                
            
            (dfs)
            1. check edge cases
            2. init a list for ans
            3. make a helper func to visit recursively
                3.1) if curLevel is eqaul to the len of the ans list, put the curVal into the list
                3.2) iterative over the right and left children of the cur node
                    3.3) if the chiild node exists, recursively call the helper func with the incremented level
        '''
                
#         res = []
#         que = deque([root])
        
#         while que:
#             rightSide = None
#             qLen = len(que)
            
#             for i in range(qLen):
#                 node = que.popleft()
#                 if node:
#                     rightSide = node
#                     que.append(node.left)
#                     que.append(node.right)
            
#             if rightSide:
#                 res.append(rightSide.val)
                
#         return res

        if not root: return []
    
        ans = []
        
        def helper(node, level):
            if level == len(ans):
                ans.append(node.val)
                
            for child in [node.right, node.left]:
                if child:
                    helper(child, level+1)
                    
        helper(root, 0)
        
        return ans