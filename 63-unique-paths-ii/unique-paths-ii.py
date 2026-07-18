class Solution(object):
    def  solve(self,i,j,m,n,dp,grid):
        if i>=m or j>=n:
            return 0
        if grid[i][j]==1:
            return 0
        if i==m-1 and j==n-1:
            return 1
        if dp[i][j]!=-1:
            return dp[i][j]
        down=self.solve(i+1,j,m,n,dp,grid)
        right=self.solve(i,j+1,m,n,dp,grid)
        dp[i][j]=right+down
        return dp[i][j]
    def uniquePathsWithObstacles(self, grid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        dp=[[-1]*n for _ in range(m)]
        return self.solve(0,0,m,n,dp,grid)

        