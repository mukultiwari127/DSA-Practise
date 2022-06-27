from ast import List


class Solution:
    
            
    def remove(self, i, j, matrix):
        m = len(matrix)
        n = len(matrix[0])
        for a in range(m):
            for b in range(n):
                if a==i:
                    if matrix[a][b] !=0:
                        matrix[a][b] = 999999
                if b==j:
                    if matrix[a][b] !=0:
                        matrix[a][b] = 999999
    
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if(matrix[i][j] == 0):
                    self.remove(i,j,matrix)
        for i in range(m):
            for j in range(n):
                if(matrix[i][j] == 999999):
                    matrix[i][j] = 0
        print(matrix)

    def setZeroesOptimized(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        dummyI = [1]*m
        dummyJ = [1]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dummyI[i]=0
                    dummyJ[j]=0
        for i in range(m):
            for j in range(n):
                if (dummyI[i]==0 or dummyJ[j]==0):
                    matrix[i][j] = 0
        print(matrix)

if __name__ == "__main__":
    a = Solution()
    input = [[1,1,1],[1,0,1],[1,1,1]]
    a.setZeroesOptimized(input)