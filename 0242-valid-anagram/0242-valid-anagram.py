class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        countS, countT = {},{}
        for char in range(len(s)):
            countS[s[char]] = countS.get(s[char], 0) + 1
            countT[t[char]] = countT.get(t[char], 0) + 1
            
        for i in countS:
            if countS[i] != countT.get(i,0): return False
            
        return True