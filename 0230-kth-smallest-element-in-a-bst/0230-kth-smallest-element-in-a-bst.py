# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        U:
            keypoints: 
                1. input tree is bst
                2. node val >= 0
                
        M: inorder dfs
        
        P:
            1. check edge case(null)
            2. init a min and prev 
            3. init a helper to visit inorder way
                3.1) if root is none: return null
                3.2) visit the left child
                3.3) put curnode into list
                3.4) visit the right child
            4. traverse the list and when k==0, return the val
                
        '''
        if not root: return 0
        ans = []
        min = 1e9
        
        def dfs(node):
            if not node: return 
            
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)
            
        dfs(root)

        for i in range(len(ans)):
            k-=1
            if k == 0: return ans[i]
        

        return -1
        