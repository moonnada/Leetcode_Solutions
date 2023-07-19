class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        '''
        U:
            key points:
                1. len(nums1) = len(num2)
                2. return the maximum possible
                
        M: minheap
        
        P: 
            1. init the result and totalSum values and a heap as an empty list
            2. create a new list by pairing two input lists and sort reversely
            3. iterate over each tuple in the merged list
                3.1) if len of heap == k, it removes the smallest element from the heap and subtract the value from nums1
                3.2) update totalsum by adding the current num1val and the it to the heap
                3.3) if len of heap == k, calculate the score
        
        
        '''
        res = 0
        totalSum = 0
        heap = []
        
        merged = [(nums2[i], nums1[i]) for i in range(len(nums1))]
        merged.sort(reverse=True)
        
        for maxOfnum2, num1val in merged:
            if len(heap) == k:
                totalSum -= heapq.heappop(heap)
                
            totalSum += num1val
            heapq.heappush(heap, num1val)
            
            if len(heap) == k:
                res = max(res, totalSum * maxOfnum2)
                
        return res