class Solution(object):
    def removeInvalidParentheses(self, s):

        def isValid(st):
            bal = 0
            for c in st:
                if c == '(': 
                    bal += 1
                elif c == ')':
                    bal -= 1
                    if bal < 0: 
                        return False
            return bal == 0

        level = {s} 
        while True:
            valid = [x for x in level if isValid(x)]
            if valid:
                return valid 
            next_level = set()
            for st in level:
                for i in range(len(st)):
                    if st[i] in ('(', ')'):
                        next_level.add(st[:i] + st[i+1:])
            level = next_level