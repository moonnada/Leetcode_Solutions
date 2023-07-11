class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        U:
           q) can grid be empty?
           q) initially rotten oranges are located in any place?
           key points: if a fresh orange keeps remaining, return -1
           
           ex) grid = [[2,1,1],
                       [0,1,1],
                       [1,0,1]]
                       
        M: BFS
        
        P:
            1. init a queue, set and time val
            2. while queue exists
                2.1) traverse around the cur position with looping
                    2.2) pop cur row and col from que
                    2.3) visit around the cur position to find whether there is a fresh orange, it it is, it gets rotten (put into queue and set
                2.4) time ++
            3. iterative the grid to find fresh oranges, if find, return -1. 
            4. return time
        '''
        
        rows , cols = len(grid), len(grid[0])
        visit = set()
        que = deque()
        time = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2: 
                    que.append((i,j))
                elif grid[i][j] == 1:
                    visit.add((i,j))
                    
        while visit and que:
            for _ in range(len(que)):
                r,c = que.popleft()
        
                for dr,dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    row,col = r+dr, c+dc
                    if 0<= row<rows and 0<=col<cols and (row, col) in visit:
                        visit.remove((row, col))
                        que.append((row,col))
                        
            time += 1
            
        return -1 if visit else time