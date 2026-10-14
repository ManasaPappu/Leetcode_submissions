class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # If the sum is greater than the maximum possible sum with 'num' digits
        if sum > num * 9:
            return ""
        
        nines = sum // 9
        remainder = sum % 9
        
        ans = ['9'] * nines
        if remainder > 0:
            ans.append(str(remainder))
        
        while len(ans) < num:
            ans.append('0')
            
        return "".join(ans)
