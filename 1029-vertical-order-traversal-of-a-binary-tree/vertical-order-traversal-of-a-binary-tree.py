# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        nodes=[]
        def dfs(node,col,row):
            if node is None:
                return
            nodes.append((col,row,node.val))
            dfs(node.left,col-1,row+1)
            dfs(node.right,col+1,row+1)
        dfs(root,0,0)
        nodes.sort()
        prev=None
        ans=[]
        for col,row,val in nodes:
            if col!=prev:
                ans.append([])
                prev=col
            ans[-1].append(val)
        return ans
            
        