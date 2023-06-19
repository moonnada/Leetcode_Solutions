class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        '''
        U: 
        q) can input arr be empty?
        
        ex) [-5,1,5,0,-7]
        => [0, -5, -4, 1,1,-6]
        => 1
        
        M: sliding window
        
        P:
            1. init an arr and its first element is 0.
            2. traverse the input arr to add each element into the created arr
            3. traverse the created arr to find a max element
            4. return the max num
        '''
        
        curHigh = 0
        highest = curHigh
        for i in gain:
            curHigh += i
            highest = max( curHigh, highest)
            
        return highest