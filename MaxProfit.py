class Solution:
    def maxProfit(self, prices):
        maxProfit = 0
        minPrice = 999999999
        for i in range(len(prices)):
            minPrice = min(minPrice, prices[i])
            maxProfit = max(maxProfit, prices[i] - minPrice)
        return maxProfit

if __name__ == "__main__":
    a = Solution()
    input = [7,1,5,3,6,4]
    print(a.maxProfit(input))