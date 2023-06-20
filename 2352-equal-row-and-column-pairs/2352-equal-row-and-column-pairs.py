class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        '''
        U:
            q) can arrs element be 2 digit numbers or negative numbers? 
            
        P: 
            1. Initialize a variable count to 0 to keep track of the number of equal row-column pairs.
            2. Iterate through each row ri from 0 to n-1:
            3.a. Iterate through each column cj from 0 to n-1:
            4. i. Check if the row ri and column cj are equal by comparing the corresponding elements.
            5.ii. If they are equal, increment the count variable by 1.
            6.Return the value of count.
        '''
        m = defaultdict(int)
        cnt = 0

        for row in grid:
            m[str(row)] += 1
        
        for i in range(len(grid[0])):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            cnt += m[str(col)]
        return cnt