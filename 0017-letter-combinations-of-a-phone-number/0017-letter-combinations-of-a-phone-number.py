class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        P:
            1. make a dic for chars
            2. init an empty list for ans
            3. traverser the input digits to put char depends on each number
            4. while the list exists,
                4.1) 
            
        '''
        dic = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        
        ans = []
        for char in digits:
            ans.append(dic[char])
            
        
        while len(ans) > 1:
            char1 = ans.pop()
            char2 = ans.pop()
            
            combined = []
            
            for i in char1:
                for j in char2:
                    combined.append(j+i)
            ans.append(combined)

        return [] if not ans else ans[0]
            