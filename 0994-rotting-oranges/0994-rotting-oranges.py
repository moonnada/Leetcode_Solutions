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
            2. traverse grid to find rotten and fresh oranges
            2. while queue and set exist
                2.1) traverse around the cur position with looping
                    2.2) pop cur row and col from que
                    2.3) visit around the cur position to find whether there is a fresh orange, if it is, it gets rotten (put into queue and set)
                2.4) time ++
            3. iterative the grid to find fresh oranges, if find, return -1. 
            4. return time
            
        time: o(nm) nm is the size of the grid. space: o(nm) n is the size of the grid, m is for the queue
        
        
        P:
            1. init a queue, time val and set
            2. traverse the input grid to find rotten and fresh oranges. if rotten oranges are found, put into queue. elif fresh is found, put into set
            3. while que exists
                3.1) visit surround of cur position by looping
                    3.2) cur position is popped from queue  
                    3.3) using a loop, visit 4 directions from the cur position
                        3.4) if a fresh orange is found within valid boundaries, remove the freshorange from set and put cur position into queue
                4.) time++
            5. return -1 if set exist otherwise time
        '''
       
        que = deque()
        visit = set()
        time = 0
        rows , cols = len(grid), len(grid[0])
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    que.append((i,j))
                elif grid[i][j] == 1:
                    visit.add((i,j))
                    
        while que and visit:
            for _ in range(len(que)):
                r,c = que.popleft()
                
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    row , col = r+dr, c+dc
                    
                    if 0<=row<rows and 0<=col<cols and (row, col) in visit:
                        visit.remove((row, col))
                        que.append((row, col))
            time+=1
            
        return -1 if visit else time
        