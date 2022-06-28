class Solution:
    
    def maxSubArray(self, nums):
        if len(nums) < 2:
            return nums[0]
        else:
            superMax = []
            for i in range(0,(len(nums))):
                window = i+1
                maxList = []
                for j in range(len(nums)-i):
                    maxList.append(sum(nums[j:(window+j)]))
                superMax.append(max(maxList))
            return max(superMax)

    def maxSubArrayOptimal(self, nums):
        meh = 0
        msf = nums[0]
        for i in range(len(nums)):
            meh += nums[i]
            if (meh>msf):
                msf = meh
            if(meh<0):
                meh = 0
        return msf

if __name__ == "__main__":
    a = Solution()
    input = [-2,1,0,4,-1,0,1,-5,4]
    print(a.maxSubArrayOptimal(input))