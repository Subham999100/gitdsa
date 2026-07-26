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
                kk=q.popleft()
                lev.append(kk.val)
                if kk.left:
                    q.append(kk.left)
                if kk.right:
                    q.append(kk.right)
            ans.append(lev)
        return ans
