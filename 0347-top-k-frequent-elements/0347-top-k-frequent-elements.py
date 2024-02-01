class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Input: nums = [1,1,1,2,2,3], k = 2
        Output: [1,2]
        
            freq:   3 2 1 0 0 0
            element:
            
            1. init a freq list and map (key: count, value: element)
            2. traverse the input list put to count and its element into map
            3. traverse the updated map to put cnt into the freq list
            4. traverse the freq list from end to start, add freq value into the ans list.
                4.1) if the ans list len == k, return ans
        '''
        
        freq = [[] for i in range(len(nums) +1) ]
        newMap = {}
        
        for i in nums:
            newMap[i] = newMap.get(i,0) + 1
            
        for num,cnt in newMap.items():
            freq[cnt].append(num)
            
        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)

                if len(res) == k: return res