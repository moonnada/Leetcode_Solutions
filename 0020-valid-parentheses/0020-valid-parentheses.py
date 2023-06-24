class Solution:
    def isValid(self, s: str) -> bool:
        '''
        U:
            q) what if s is empty?
            
            ex) s = "[ { (  ) } ]"
            
        M: stack
        
        P:  
            0. check edge case( if len(s) % 2 ==1, false)
            1. init a stack
            2. traverse the input str to put each char into stack
                2.1) check cur char is any open parentheses. if it is, put into stack
                
        '''
          # Create a pair of opening and closing parrenthesis...
        opcl = dict(('()', '[]', '{}'))
        # Create stack data structure...
        stack = []
        # Traverse each charater in input string...
        for idx in s:
            # If open parentheses are present, append it to stack...
            if idx in '([{':
                stack.append(idx)
            # If the character is closing parentheses, check that the same type opening parentheses is being pushed to the stack or not...
            # If not, we need to return false...
            elif len(stack) == 0 or idx != opcl[stack.pop()]:
                return False
        # At last, we check if the stack is empty or not...
        # If the stack is empty it means every opened parenthesis is being closed and we can return true, otherwise we return false...
        return len(stack) == 0