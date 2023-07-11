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
            1. check edge cases
            2. traverse the maze list to find exits. if find, put the val into a list
            3. once exits list is ready, compare with entrance by looping
        '''
        
        rows, cols = len(maze), len(maze[0])
        start = tuple(entrance)
        que = deque([start])
        res = 0
        visit = set([start])
        
        while que:
            for i in range(len(que)):
                r,c = que.popleft()
                if [r,c] != entrance and (r==0 or c==0 or r==rows-1 or c == cols-1):
                    return res
                
                for dr, dc in [(1,0), (0,1), (-1,0), (0,-1)]:
                    row, col = r+dr, c+dc
                    if 0<=row<rows and 0<=col<cols and maze[row][col] =="." and (row,col) not in visit:
                        que.append((row,col))
                        visit.add((row,col))
                        
            res += 1
            
        return -1