from itertools import permutations

class Solution:
    
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        firstIndex = -1
        secondIndex = -1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                firstIndex = i
                break
        if firstIndex<0:
            nums.reverse()
        else:
            for i in range(len(nums)-1,(firstIndex-1),-1):
                if nums[i] > nums[firstIndex]:
                    secondIndex = i
                    break
            temp = nums[firstIndex]
            nums[firstIndex] = nums[secondIndex]
            nums[secondIndex] = temp
            temp = nums[(firstIndex+1):]
            temp.reverse()
            temp = nums[:(firstIndex+1)] + temp
            for i in range(len(nums)):
                nums[i] = temp[i]
            print(nums)

if __name__ == "__main__":
    a = Solution()
    input = [2,1,3,4,6]
    a.nextPermutation(input)