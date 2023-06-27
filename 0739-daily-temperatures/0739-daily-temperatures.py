class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        U: 
            key points: can be below 30, no future day then put 0 
            
            ex) t = [73, 74, 75, 71, 69. 72, 76, 73]
              ans = [1,1,4,2,1,1,0,0]
              
        M: stack
        
        curVal = 71
        stack = [75,71]
        ans = [1,1, ]
        
        if stack[-1] < curVal:
            ans.add( curVal - stack[-1])
            stack.pop()
            stack.append(curVal)
        else
            stack.append(curVal)
        '''
        
        res = [0] * len(temperatures)
        stack = [] #pair: [temp, index]
        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackIndex = stack.pop()
                res[stackIndex] = (i - stackIndex)
                
            stack.append([t,i])
        
        return res