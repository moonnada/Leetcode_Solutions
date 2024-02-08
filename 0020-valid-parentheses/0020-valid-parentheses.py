class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        pairs = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        
        for i in s:
            if i in pairs:
                stack.append(i)
            elif not stack or pairs[stack[-1]] != i:
                return False
            else:
                stack.pop()
        
        return not stack 
                
        
        