class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        U:
            q) input str can have any letter?
            
        M: two ptrs
        
        P:
            1. take care of edge cages (empty, one letter)
            2. init two val for left and right
            3. while left < right, check whether each letter is lowercase letter and non-alphabetical letter
            4. in the loop, check whether each letter is the same. if it is, then left++, right--
        '''
        
        left = 0
        right = len(s)-1
        
        while left < right:
            while left < right and not s[left].isalnum():
                left +=1
            while left < right and not s[right].isalnum():
                right-=1
                
            if left < right and s[left].lower() != s[right].lower():
                return False
            
            left+=1
            right-=1
            
        return True