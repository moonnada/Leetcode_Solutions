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
            3. init a helper to visit inorder way
                3.1) if root is none: return null
                3.2) visit the left child
                3.3) put curnode into list
                3.4) visit the right child
            4. traverse the list and when k==0, return the val
                
        '''
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
                
            if not stack: break
        
            node = stack.pop()
            k -= 1
            
            if k == 0: return node.val
            
            root = node.right