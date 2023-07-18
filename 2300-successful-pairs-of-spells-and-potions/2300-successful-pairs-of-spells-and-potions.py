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
        list1=[]
        potions.sort()
        # // some test cases are not sorted
        for s in spells:
            # // binary search on left most value i.e greater than success
            left,right,index=0,len(potions)-1,len(potions)# index is len(potions) in worst case where no values matches with potions values
            while left<=right:
                mid=(left+right)//2
                if s*potions[mid]>=success:
                    right=mid-1
                    index=mid
                else:
                    left=mid+1
            # // add all possible values by total length -index
            list1.append(len(potions)-index)
        return list1
#         potions.sort()
#         ans = []
        
#         for spell in spells:
#             left , right,idx = 0, len(potions)-1, len(potions)
            
#             while left <= right:
#                 mid = left + (right-left) // 2
                
#                 if spell * potions[mid] >= success:
#                     right = mid -1
#                     idx = right
#                 else:
#                     left = mid + 1
                    
#             ans.append(len(potions) - idx)
        
#         return ans
        
        