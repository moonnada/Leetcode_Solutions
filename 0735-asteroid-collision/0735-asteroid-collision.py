class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
        U:
            q) always positive nums are on the left side and negative num are on the right side? 
                ex) [7,-3,9,3,-1,3] => this wouldnt be considered?
                
                
            ex) [5,10,2,-5,-3,-9]
                         p
                 
            set: 5,10,-5
        
        M: set, sliding window
        
        P: - traverse the input list 
                - if curElement > 0, put the set
                  else compare the absValues of culElement and the last val of set. put the bigger one into the set. while set has a negative num, keep comparing
                  
        
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