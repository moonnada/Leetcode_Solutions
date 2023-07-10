# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        '''
        U:
            keypoints: 
            1. tree is BST
            2. input tree is not empty
            3. if val is not in tree, return null
            
            q) input tree can have the same val multiple times?
                
        M: DFS
        
        P: 
            1. check edge case(null)
            2. if targetVal < root, visit left. elif val = root.val, put into ans list. else visit right.
        '''
        if not root or val == root.val: return root
        
        return self.searchBST(root.left,val) if val < root.val else self.searchBST(root.right , val)