class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        '''
        U:
        q) what if two input strs lengths are different?
        q) can two input strs be empty?
        
        ex) 'cabbba'  ,  'abbccc'
          1. caabbb       abbccc
          2. baaccc
          3. abbccc
          
        M: hashmap, sliding window
        
        P: 
            1. check edge cases(empty, different lengths)
            2. counts the occurrence of letters in two words
            3. if letters and occurrence are the same, return true else false
        '''
        
        if len(word1) != len(word2): return False
    
        c1 = Counter(word1)
        c2 = Counter(word2)
        
        n1 = Counter([v for v in c1.values()])
        n2 = Counter([v for v in c2.values()])
        
        return c1 == c2 or ( n1 == n2 and set(word1) == set(word2))