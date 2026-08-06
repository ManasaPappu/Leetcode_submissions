class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        
        while True:
    
            temp = n
            product = 1
            
            
            if temp == 0:
                product = 0
                
            while temp > 0:
                product *= temp % 10
                temp //= 10
            
            if product % t == 0:
                return n
            
            n += 1
