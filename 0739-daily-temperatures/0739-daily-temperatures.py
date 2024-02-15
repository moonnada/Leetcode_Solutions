class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        Input: temperatures = [73,74,75,71,69,72,76,73]
        Output: [1,1,4,2,1,1,0,0]
        
        1. init a stack and an ans list
        2. iterative the input list from 1 to end 
           
        
        '''
        
        res = [0] * len(temperatures)
        stack = []
        
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackIdx = stack.pop()
                res[stackIdx] = i - stackIdx
            
            stack.append([t,i])
            
        return res