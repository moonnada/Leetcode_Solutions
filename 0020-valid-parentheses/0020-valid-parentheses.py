class Solution:
    def isValid(self, s: str) -> bool:
        '''
        stack
        
        1. init a stack
        2. init a dic for valid parentheses
        3. iterative the input str to find valid parenthese
            3.1) if cur char is an open bracket, append it to the stack
            3.2) else if stack is empty or cur char is not matched with the recent stack val, return False
            3.3) else pop from stack
        4. return true if stack is empty
        '''
        
        stack = []
        valid = { 
        '(' : ')',
        '{' : '}',
        '[' : ']'
        }
        
        for i in s:
            if i in valid:
                stack.append(i)
            elif not stack or valid[stack[-1]] != i: 
                return False
            else:
                stack.pop()
        return True if not stack else False