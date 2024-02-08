class Solution:
    def isValid(self, s: str) -> bool:
        '''
        1. loop the input s and if one of closed parentheses is found, pop its open bracket
        2. else // open bracket, push it to the stack
        '''
        
        stack = []
        pairs = {
            '(': ')',
            '{': '}',
            '[':']'
        }
        
        for i in s:
            if i in pairs:
                stack.append(i)
            elif len(stack) == 0 or i != pairs[stack.pop()]:
                return False
            
        return len(stack) == 0