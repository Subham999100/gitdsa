class Solution(object):
    def solve(self,i,j,m,n,dp,grid):
        if i==m-1 and j==n-1:
            return grid[i][j]
        if dp[i][j]!=-1:
            return dp[i][j]
        if i==m-1:
             dp[i][j]= grid[i][j]+self.solve(i,j+1,m,n,dp,grid)
        elif(j==n-1):
             dp[i][j]=grid[i][j]+self.solve(i+1,j,m,n,dp,grid)
        else:
             dp[i][j]=grid[i][j]+min(self.solve(i,j+1,m,n,dp,grid),self.solve(i+1,j,m,n,dp,grid))
        return dp[i][j]
        
            
        
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        dp=[[-1]* n for _ in range(m)]
        return self.solve(0,0,m,n,dp,grid)
        