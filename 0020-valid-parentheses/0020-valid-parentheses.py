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
        stack, hm = [], {'(': ')', '{': '}', '[': ']'}
        for ch in s:
			# open bracket
            if ch in '({[': 
                stack.append(ch)
			# close bracket
            else: 
                if not stack or hm[stack[-1]] != ch: return False
                stack.pop()

        return not stack