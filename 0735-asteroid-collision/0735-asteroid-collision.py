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
                  
        
        '''
        stack = []

        # Iterate over asteroids
        for asteroid in asteroids:
            
            # if stack top is positive and asteroid is negative
            while stack and stack[-1] > 0 and asteroid < 0:

                # if asteroid is greater then remove the current stack top element
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                    continue
                
                # If equal remove top and dont add current asteroid
                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                break

            else:
                stack.append(asteroid)

        # return Stack
        return stack
#         stack = []
        
#         for num in asteroids:
            
#             while stack and stack[-1] > 0 and num < 0:
                
#                 if abs(stack[-1]) < abs(num):
#                     stack.pop()
#                     continue
                    
#                 elif abs(stack[-1]) == abs(num):
#                     stack.pop
#                 break
                
#             else:
#                 stack.append(num)
        
#         return stack

          