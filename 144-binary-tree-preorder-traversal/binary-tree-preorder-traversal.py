# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def preorder(self,root,ans):
        if root is None:
            return
        ans.append(root.val)
        self.preorder(root.left,ans)
        self.preorder(root.right,ans)

    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ans=[]
        self.preorder(root,ans)
        return ans
        