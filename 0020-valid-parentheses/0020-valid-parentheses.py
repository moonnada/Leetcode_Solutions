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
                2.2) else if stack is not empty and top of stack is not equal to the curval, return false. else pop
            3. return stack is empty as true
                
        '''
        stack = []
        hm =  {'(' : ')', '{': '}', '[': ']'} 
        
        for i in s:
            if i in hm:
                stack.append(i)
            else:
                if not stack or hm[stack[-1]] != i:
                    return False
                else:
                    stack.pop()
        return not stack