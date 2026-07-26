# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def order(self,root,ans):
        if root is None:
            return
        self.order(root.left,ans)
        self.order(root.right,ans)
        ans.append(root.val)    
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ans=[]
        self.order(root,ans)
        return ans
        