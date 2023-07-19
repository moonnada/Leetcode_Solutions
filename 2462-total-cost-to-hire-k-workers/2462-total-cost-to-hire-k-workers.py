class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        '''
        U:  
                         0  1  2  3 4 5 6  7  8
            ex) costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
            k sessions
            1: [17,12,10,2] => (3), 2. cost = 2
            2: [17,12,10,7,2,11,20,8] => (4), 2. cost = 4
            3: [17,12,10,7,11,20,8] => (3), 7. cost = 11
            
            
        M: minheap
        
        P: 
           1. init a heap list
           2. iterative over the costs list
            2.1) if len of heap == candidiates and k >0, get the min element using heappop. cost += min. k--
            2.2) else put the cur element into heap
            
        '''
        n = len(costs)
        heap = []
        left , right = candidates, n-candidates-1
        
        for i in range(candidates):
            heapq.heappush(heap, (costs[i],i))
            
        for i in reversed(range(n-candidates, n)):
            if i < left: break
                
            heapq.heappush(heap, (costs[i], i))
            
        totalCost = 0
        
        for _ in range(k):
            cost, idx = heapq.heappop(heap)
            totalCost += cost
            
            if left <= right:
                if idx < left:
                    heapq.heappush(heap, (costs[left], left))
                    left += 1
                    
                elif idx > right:
                    heapq.heappush(heap, (costs[right], right))
                    right -= 1
        
        return totalCost