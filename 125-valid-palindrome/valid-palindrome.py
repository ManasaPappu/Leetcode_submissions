class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string = "".join([char for char in s if char.isalnum()])
        string = string.lower()
        if string == string[::-1]:
            return True
        else:
            return False