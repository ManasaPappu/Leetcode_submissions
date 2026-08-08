class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1 
        ite = 0
        
        while ite <= right:   
            if nums[ite] == 0: 
                nums[left], nums[ite] = nums[ite], nums[left]
                left += 1
                ite += 1      
                
            elif nums[ite] == 2:
                nums[right], nums[ite] = nums[ite], nums[right]
                right -= 1     
                
            else:
                ite += 1
