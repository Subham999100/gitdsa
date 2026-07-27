# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def height(self,root):
        if root is None:
            return 0
        lf=self.height(root.left)
        rg=self.height(root.right)
        return 1+max(lf,rg)
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return True
        lefth=self.height(root.left)
        righth=self.height(root.right)
        if(abs(lefth-righth)>1):
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        