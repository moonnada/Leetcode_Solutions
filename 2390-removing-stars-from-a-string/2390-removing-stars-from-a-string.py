class Solution:
    def removeStars(self, s: str) -> str:
        '''
        U: 
            q) what if str has only *?
        
        P:
            1. check edge case(empty)
            2. init an arr for answer
            3. traverse the input str to put elements into arr
        '''
        
        
        
        if len(s) == 0: return ""
        
        ans=[]
        
        for i in s:
            if i!='*':
                ans+=[i]
            else:
                ans.pop()
        return "".join(ans)