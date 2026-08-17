class Solution(object):
    def maximumSubarraySum(self, nums, k):
        seen = set()
        answer = 0
        current = 0
        left = 0
        for i in range (len(nums)):
            while nums[i] in seen:
                seen.remove(nums[left])
                current -= nums[left]
                left+=1
            seen.add(nums[i])
            current += nums[i]
            if i - left + 1 == k:
                answer = max(answer,current)
                seen.remove(nums[left])
                current -= nums[left]
                left += 1
        return answer




