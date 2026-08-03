class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = list(nums)
        n.sort()
        largest = n[-1]
        sec_largest = n[-2]
        return (largest-1) * (sec_largest-1)
        