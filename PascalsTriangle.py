class Solution:
    def generate(self, numRows):
        output = [[1]]
        if numRows>=2: 
            output = [[1],[1,1]]
            for i in range(2,numRows):
                output.append([1]*(i+1))
                for j in range(1,i):
                    if (j>0 and j<i):
                        output[i][j] = output[i-1][j-1] + output[i-1][j]
        return output

if __name__ == "__main__":
    a = Solution()
    input = 8
    print(a.generate(input))