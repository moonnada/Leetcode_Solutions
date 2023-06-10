class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        U:
            q) input arr can be empty?
            q) what should i return if there is the same count but k is not sufficient
            
        num: [1,1,1,2,2,3] k=2 => [1,2]
        
        M : 
            hashmap (key: count, val: number), bucketsort
            
        P :
            1. init a map
            2. iterate a loop to put key and val inside the map
            3. iterate a loop to put number and its count from map to bucket
            4. init a result arr
            5. traverse the bucket from at the end to start
                5.1. make a loop to put result arr
                5.2. if the result arr's lentgh is same as k, then just return the arr
        '''
        
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for i in nums:
            count[i] = count.get(i, 0) + 1
            
        for num, cnt in count.items():
            freq[cnt].append(num)
            
        result = []
        
        for i in range(len(freq)-1, 0 ,-1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
        
        
        
        
        
        
        
        
#         count = {}  # hashmap (key: count, val: number)
#         freq = [[] for i in range(len(nums) + 1)] # bucket sort. init a bucket
        
#         for n in nums: #put key and count into map
#             count[n] = count.get(n,0) + 1
            
#         for n, cnt in count.items(): #add number based on count as a key
#             freq[cnt].append(n)
            
#         res = []
#         for i in range(len(freq)-1, 0, -1):
#             for n in freq[i]:
#                 res.append(n)
#                 if len(res) == k:
#                     return res

        