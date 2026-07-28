# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.maxi=float('-inf')
        def sumi(groot):
            if groot is None:
                return 0
            lf=sumi(groot.left)
            rg=sumi(groot.right)
            koiacha=lf+rg+groot.val
            ekacha=max(lf,rg)+groot.val
            rootacha=groot.val
            self.maxi=max(self.maxi,koiacha,ekacha,rootacha)
            return max(ekacha,rootacha)
        sumi(root)
        return self.maxi
        