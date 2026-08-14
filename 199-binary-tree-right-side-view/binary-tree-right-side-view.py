# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorder(self,root,lev,res):
        if root is None:
            return
        if len(res)<lev:
            res.append(root.val)
        self.preorder(root.right,lev+1,res)
        self.preorder(root.left,lev+1,res)

    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res=[]
        self.preorder(root,1,res)
        return res
        