class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        t = 0
        r =0
        for i in nums:
            if i :
                r = r+1
            else:
                if r > t:
                    t = r
                r=0
        if r > t:
            t = r
        return t