# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        def isSameTree(root, subRoot):
            if not root and not subRoot:
                return True
            
            if root and subRoot and root.val == subRoot.val:
                return isSameTree(root.left, subRoot.left) and isSameTree(root.right, subRoot.right)
            else:
                return False
        
        if root and subRoot:
            queue = [root]
            while queue:
                # for i in range(len(queue)):
                curNode = queue.pop(0)
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
                if curNode.val == subRoot.val:
                    if isSameTree(curNode, subRoot):
                        return True
        return False
    
            
#         if not root: 
#             return False
        
#         def isSameTree(root, subRoot):
#             if not root and not subRoot:
#                 return True
            
#             if root and subRoot:
#                 return root.val == subRoot.val and isSameTree(root.left, subRoot.left) and isSameTree(root.right, subRoot.right)
            
#         if isSameTree(root, subRoot): return True 
        
#         return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        
        