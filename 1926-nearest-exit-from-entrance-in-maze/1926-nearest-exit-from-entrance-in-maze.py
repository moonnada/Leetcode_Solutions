class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        '''
        U:
            keypoints: 
                1. if no path exists, return -1
                2. can move up, down, left and right only
                3. need to find exits first
                
            ex) maze = [["+","+",".","+"],
                        [".",".",".","+"],
                        ["+","+","+","."]]
                        
        M: BFS => shortest path 
                        
        P:
            1. init cols and rows 
            2. init a queue, set and result
            3. while queue exists
                3.1) pop a row and col from queue
                3.2) check whether cur row and col is on exit. if it is return the result
                    3.3) make a loop to visit every direction. if cur position is not a wall and not visited, put the position into que and set
                3.4) result is incremented
        '''
        
        rows, cols = len(maze), len(maze[0])
        start = tuple(entrance)
        que = deque([start])
        visit = set([start])
        res = 0
        
        while que:
            
            for i in range(len(que)):
                r,c = que.popleft()
                if [r,c]!= entrance and (r == 0 or c==0 or r==rows-1 or c == cols-1):
                    return res

                for dr,dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    row, col = r+dr, c+dc
                    if 0<=row<rows and 0<=col<cols and maze[row][col] == "." and (row,col) not in visit:
                        que.append((row,col))
                        visit.add((row, col))

            res+=1
            
        return -1
        
        