class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        '''
        P:
            1. sort the potion list
            2. init a ans list
            3. traverse the spells list to find success number
                3.1) init two ptrs and idx val as len of potion list
                3.2) while left <= right:
                    3.3) get the mid val
                    3.4) if the product of two lists >= success, rearrange of the right and index val
                    3.5) else, update the left val
                3.6) put len of potions - idx into the ans list
                
        time: o(nlgn) , space: o(n) n is for the ans list
        
        
        P:
            1. sort the potions list
            2.  the ans list
            3. traverse the spells list to find valid success
                3.1) init two ptrs as left and right and init the idx val as potions length
                3.2) traverse the sorted potions list
                    3.3) init the mid point
                    3.4) if spell elemnt * potion[mid] > success, right = mid -1, idx = mid
                    3.5) if spell elemnt * potion[mid] < success, left = mid +1
                3.6) put len of potions - idx 
        '''
        
        potions.sort()
        ans = []
        
        for spell in spells:
            left , right,idx = 0, len(potions)-1, len(potions)
            
            while left <= right:
                mid = left + (right-left) // 2
                
                if spell * potions[mid] >= success:
                    right = mid -1
                    idx = mid
                else:
                    left = mid + 1
                    
            ans.append(len(potions) - idx)
        
        return ans
        
        