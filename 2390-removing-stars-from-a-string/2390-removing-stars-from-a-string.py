class Solution:
    def removeStars(self, s: str) -> str:
        ans=[]
        
        if len(s) == 0: return ""
        
        for i in s:
            if i=='*':
                ans.pop()
            else:
                ans+=[i]
        return "".join(ans)