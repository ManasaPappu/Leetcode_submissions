class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        bits = [sum((n >> i) & 1 for n in nums) for i in range(30)]
        
        ans = 0
        for _ in range(k):
            num = sum((1 << i) for i in range(30) if bits[i] > 0)
            for i in range(30): 
                if bits[i] > 0: bits[i] -= 1
            ans += num * num
            
        return ans % 1_000_000_007
