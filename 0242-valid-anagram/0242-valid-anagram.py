class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        '''
        U: 
        q) can input str be empty?
        q) any letter can be in input str?
        
        M: 
        hashmap (key: num, val: cnt)
        
        p:
        1. check each str's length and if they are different, return false
        2. init maps for the two input strs to count
        3. traverse the first input str to put key and value inside a map. put input s, t both
        4. traverse the input s'map to compare t's map count
        
        I: 
        
        R: 
            time: o(n), space: o(n)
        '''
        
        if len(s) != len(t): return False
        
        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
            
        for cnt in countS:
            if countS[cnt] != countT.get(cnt,0): return False
            
        return True
    