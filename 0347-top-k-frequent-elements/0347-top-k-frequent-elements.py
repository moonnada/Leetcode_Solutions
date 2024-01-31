class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
#         q) is the input list sorted?
#             hashmap (key: cnt, value: elements)
    
#         0. init a hashmap and freq list
#         1. traverse the input list to put key and value into the map
#         2. traverse the hashmap to put each element and count into the freq list
#         3. traverse the freq from end to start
#             3.1) iterative a number in the freq to put elements into ans list
#             3.2) if len of ans list == k, return ans


        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for i in nums:
            count[i] = count.get(i, 0)+1
            
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        
        
        res = []
        
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                
                if len(res) == k: return res