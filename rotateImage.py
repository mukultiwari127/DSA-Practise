class Solution:
    
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        dummyMatrix = []
        for j in range(len(matrix[0])):
            tuple = []
            for i in range(len(matrix)-1, -1, -1):
                tuple.append(matrix[i][j])
            dummyMatrix.append(tuple)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = dummyMatrix[i][j]
        return matrix
                
if __name__ == "__main__":
    a = Solution()
    input = [[1,2,3],[4,5,6],[7,8,9]]
    print(a.rotate(input))