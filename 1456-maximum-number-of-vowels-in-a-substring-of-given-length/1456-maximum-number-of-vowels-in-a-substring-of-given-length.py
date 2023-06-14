class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        '''
        U:
        q) input str can have any letter or only lowercase letter
        
        ex) leetcode, k=3
        
        
        M: sliding window
        
        P:
            1. init a set and put letters of input str within 'k' val into the set
            2. make a str for vowel letters
            3. 
        '''
        VOWELS = frozenset('aeiou')
        
        cnt=cur= left = 0
        
        for right in range(len(s)):
            if s[right] in VOWELS:
                cur += 1
                
            if right - left + 1 > k:
                if s[left] in VOWELS:
                    cur -= 1
                left += 1
                
            cnt = max(cnt, cur)
            
        return cnt