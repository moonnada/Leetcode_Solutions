class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        U: 
            key points: can be below 30, no future day then put 0 
            
            ex) t = [73, 74, 75, 71, 69. 72, 76, 73]
              ans = [1,1,4,2,1,1,0,0]
              
        M: stack
        
        P: 
            1. init a res list. put 0 as much as len of input list
            2. init a stack
            3. traverse the input list to put index and value of list
                3.1) while stack and curVal > stack's top
                    3.2) pop temp and index from stack
                    3.3) put curIndex - stackIndex into ans list. 
                4) put cur temp and index into stack
            5. return list
            
        
        t: o(n), s: o(n)
        '''
        
        res = [0] * len(temperatures)
        stack = [] 
        
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            
            stack.append([t, i])
            
        return res