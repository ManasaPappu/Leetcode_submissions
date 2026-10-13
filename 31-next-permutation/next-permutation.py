class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = next((i for i in range(len(nums) - 2, -1, -1) if nums[i] < nums[i+1]), -1)
        if i >= 0:
            j = next(j for j in range(len(nums) - 1, i, -1) if nums[j] > nums[i])
            nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = reversed(nums[i+1:])
