class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Sort the array in ascending order
        nums.sort()
    
        product_positives = nums[-1] * nums[-2] * nums[-3]
        
        product_negatives = nums[0] * nums[1] * nums[-1]
        return max(product_positives, product_negatives)
