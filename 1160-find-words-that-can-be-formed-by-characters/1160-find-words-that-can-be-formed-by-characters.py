class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        '''
        1. init a dict
        2. put key and value from the input str (char, cnt)
        3. traverse the input list 
        '''
        count = Counter(chars)
        res = 0
        
        for word in words:
            cur_word = defaultdict(int)
            good = True
            
            for char in word:
                cur_word[char] += 1
                if char not in count or cur_word[char] > count[char]:
                    good = False
                    break
            
            if good:
                res += len(word)
        return res