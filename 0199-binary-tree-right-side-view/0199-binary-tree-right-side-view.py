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
            q) tree can have a same num multiple times?
        
        M: BFS
        
        P: 
            1. check edge case(null)
            2. init a que and ans list
            3. while que exists
                3.1) init a rightside as none
                3.2) looping cur level to put each side value into queue
                    3.3) curnode is popped from queue
                    
                3.4) if rightside val exists, put the val into ans list
            4. return ans
        '''
        
        ans = []
        que = deque([root])
        
        while que:
            rightSide = None
                        
            for _ in range(len(que)):
                curNode = que.popleft()
                
                if curNode:
                    rightSide = curNode
                    que.append(curNode.left)
                    que.append(curNode.right)
                
            if rightSide:
                ans.append(rightSide.val)
                
        return ans
        