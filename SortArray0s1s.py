class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        blue = []
        white = []
        red = []
        for elem in nums:
            if elem == 0:
                red.append(elem)
            elif elem == 1:
                white.append(elem)
            else:
                blue.append(elem)
        red.extend(white)
        red.extend(blue)
        for i in range(len(nums)):
            nums[i] = red[i]
        print(nums)

if __name__ == "__main__":
    a = Solution()
    input = [2,0,2,1,1,0]
    a.sortColors(input)
        