class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        k = k1 + k2
        diffs = [abs(n1 - n2) for n1, n2 in zip(nums1, nums2)]
        max_diff = max(diffs)
        
        if sum(diffs) <= k:
            return 0
            
        bucket = [0] * (max_diff + 1)
        for d in diffs:
            bucket[d] += 1
            
        for d in range(max_diff, 0, -1):
            if bucket[d] > 0:
                ops = min(bucket[d], k)
                bucket[d] -= ops
                bucket[d - 1] += ops
                k -= ops
                
                if k == 0:
                    break
                    
        return sum(count * (d ** 2) for d, count in enumerate(bucket))
