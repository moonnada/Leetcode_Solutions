class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
        U:
            q) always positive nums are on the left side and negative nums are on the right side? 
                ex) [7,-13,19,3,-1,3] => is it a valid example?
                
        M: stack
        
        P: 
            1) init a stack
            2) iterate over the input list
                2.1) while stack top is positive and new number is negative
                        2.2) if stack top < new number, stack.pop and continue
                        2.3) elif stack top == new number, stack pop
                        2.4) break
                2.5) add the curVal into the stack
                  
        time: o(n), space: o(n)
        '''
        stack = []
        
        for num in asteroids:
            
            while stack and stack[-1] > 0 and num < 0:
                
                if abs(stack[-1]) < abs(num):
                    stack.pop()
                    continue
                    
                elif abs(stack[-1]) == abs(num):
                    stack.pop()
                break
                
            else:
                stack.append(num)
        
        return stack

          