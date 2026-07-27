# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.dia=0
        def heigh(no):
            if no is None:
                return 0
            le=heigh(no.left)
            ri=heigh(no.right)
            self.dia=max(self.dia,le+ri)
            return 1+max(le,ri)
        heigh(root)
        return self.dia
        