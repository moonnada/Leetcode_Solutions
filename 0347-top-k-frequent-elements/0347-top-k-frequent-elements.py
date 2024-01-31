class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
#         q) is the input list sorted?
        
#         1. init a hashmap(key: element, value: count of its element)
#         2. traverse the input list to put value in the map
#             2.1) add the cur element into map
#             2.2) if count of cur element >= k, add into ans list 
#         3.return ans list
        
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        
        for i in nums:
            count[i] = count.get(i,0) + 1
            
        for num, cnt in count.items():
            freq[cnt].append(num)
            
        res = []
        
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                
                if len(res) == k:
                    return res