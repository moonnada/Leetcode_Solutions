class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
        U:
        q) what should i return if both input arrs are empty
        q) 
        ex) 
        s= "abc", t="ahbgdc"
            L        R
             L         R
             
        
        M: two ptrs
        
        P: 
        1. check edge cases(empty, compare each str length)
        2. init a two ptrs for each str
        3. traverse the longest arr to check there is subsequnece or not
    
        '''
        
        if len(s) > len(t): return False
        
        left, right = len(s), len(t)
        p_left = 0
        p_right = 0
        while p_left < left and p_right < right:
            if s[p_left] == t[p_right]:
                p_left += 1
            p_right += 1
        
        return p_left == left
            
           
        
        