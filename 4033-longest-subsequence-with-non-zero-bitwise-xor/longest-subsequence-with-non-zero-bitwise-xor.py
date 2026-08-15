class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        xor_sum = 0
        for num in nums:
            xor_sum ^= num
        if all(num == 0 for num in nums):
            return 0
        if xor_sum != 0:
            return len(nums)
        return len(nums) - 1