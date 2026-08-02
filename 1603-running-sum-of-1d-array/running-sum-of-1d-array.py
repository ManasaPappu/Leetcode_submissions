class Solution(object):
    def runningSum(self, nums):
        running_sum = 0
        ans = []

        for i in range(len(nums)):
            running_sum += nums[i]
            ans.append(running_sum)

        return ans