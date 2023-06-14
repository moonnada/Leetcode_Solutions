class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        '''
        U:
        q) input str can have any letter or only lowercase letter
        
        ex) leetcode, k=3
        
        
        M: sliding window
        
        P:
            1. init a str for vowel letters
            1. init values( cnt, cur, left) as 0
            3. traverse the input arr
                3.1) if a vowel is found in a position, then cnt ++
                3.2) if traversed length > k 
                3.3)       if cur position has a vowel, then cnt--
                3.4) left++
                3.5) get max
            4. return max
                
        '''
      
        VOWELS = 'aeiou'
        
        maxVowels = cur = left = 0
        
        for right in range(len(s)):
            if s[right] in VOWELS:
                cur+= 1
                
            if right - left + 1 > k:
                if s[left] in VOWELS:
                    cur-=1
                left +=1
            
            maxVowels = max(cur , maxVowels)
            
        return maxVowels