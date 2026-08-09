class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
       
        if s == s[::-1]:
            return s
            
        n = len(s)
        
        for length in range(n, 0, -1):
            for i in range(n - length + 1):
                j = i + length
                
                substring = s[i:j]
                if substring == substring[::-1]:
                    return substring
