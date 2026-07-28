# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q=deque([root])
        ans=[]
        lfrg=True
        while q:
            lev=[]
            size=len(q)
            for _ in range(size):
                node=q.popleft()
                lev.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if not lfrg:
                lev.reverse()
            ans.append(lev)
            lfrg=not lfrg
        return ans
                


        