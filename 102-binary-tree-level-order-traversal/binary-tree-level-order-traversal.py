from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q=deque([root])
        ans=[]
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
            ans.append(lev)
        return ans
