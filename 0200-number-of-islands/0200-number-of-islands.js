/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
 /*
 backtracking dfs
 1. traverse 2d arr and find the first "land" and visit after the first land recursively. cnt is incremented
 2. in a helper func, check edge cases first. and then if cur position is land, then change to water to avoid revisit
 3. dfs 4 ways
 */
    
    let row = grid.length;
    let col = grid[0].length; 
    let cnt = 0;
    
    for(let i=0; i<row; i++){
        for(let j=0; j<col; j++){
            if(grid[i][j] === "1"){
                cnt++;
                dfs(i,j,grid)
            }
        }
    }
    
    function dfs(i,j, grid){
        if(i<0 || i>= grid.length || j<0 || j>=grid[0].length) return;
        
        if(grid[i][j] === "1"){
            grid[i][j] = "0";
            
        } else return
        
        dfs(i-1,j,grid);
        dfs(i+1,j,grid);
        dfs(i,j-1,grid);
        dfs(i,j+1,grid);
    }
    
    return cnt;
}