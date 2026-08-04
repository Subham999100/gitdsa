class Solution(object):
    def find(self,board,i,j,idx,word,m,n):
        if idx==len(word):
            return True
        if(i<0 or j<0 or i>=m or j>=n or board[i][j]=='$'):
            return False
        if(board[i][j]!=word[idx]):
            return False
        temp=board[i][j]
        board[i][j]='$'
        found=(
            self.find(board,i+1,j,idx+1,word,m,n) or
            self.find(board,i-1,j,idx+1,word,m,n) or
            self.find(board,i,j+1,idx+1,word,m,n) or
            self.find(board,i,j-1,idx+1,word,m,n)
        )
        board[i][j]=temp
        return found


    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m=len(board)
        n=len(board[0])
        for i in range(m):
            for j in range(n):
                if(board[i][j]==word[0] and self.find(board,i,j,0,word,m,n)):
                    return True
        return False