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
            else:
                if not stack or pairs[stack[-1]] != i:
                    return False
                else:
                    stack.pop()
            
        return len(stack) == 0