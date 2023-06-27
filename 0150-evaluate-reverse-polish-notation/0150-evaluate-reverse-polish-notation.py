class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        U:
            q) do I return always integer when I divide each num
            q) can input list have operators first?
            
            ex) [2,1,+,3,5,-]
            
            s = [2,1]
            
            
            
        M: stack
        
        P: 
            1. init a stack
            2. traverse the input list to put val into stack
                2.1) if curVal is num, put into stack
                2.2) if not, calculate the second top of stack and top of stack. once calculating is done, put the new val into stack\
            3. return ans
        
        
        '''
        ans = 0
        stack = []
        
        
        for i in tokens:
            if i not in "+-*/":
                stack.append(int(i))
                continue
            
            num2 = stack.pop()
            num1 = stack.pop()
            
            if i == "+":
                ans = num1 + num2
            
            elif i == "*":
                ans = num1 * num2
                
            elif i == "-":
                ans = num1 - num2
                
            elif i == "/":
                ans = int(num1 / num2)
                
            stack.append(ans)
            
        return stack.pop()
        