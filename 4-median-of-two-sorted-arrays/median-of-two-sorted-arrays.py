class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        combined = nums1 + nums2
        combined = sorted(combined)
        n = len(combined)
        if len(combined) % 2 == 0:
            middle = n//2
            return (combined[middle] + combined[middle - 1]) / 2.0
        else: 
            middle = n//2
            return combined[middle]