# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: str
        """
        if root is None:
            return ""
        result=str(root.val)
        left=self.tree2str(root.left)
        right=self.tree2str(root.right)
        if(root.left is None and root.right is None):
            return result
        if(root.left is None):
            return result+"()"+"("+right+")"
        if(root.right is None):
            return result+"("+left+")"
        
        return result+"("+left+")"+"("+right+")"



        