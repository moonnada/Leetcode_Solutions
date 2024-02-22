/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    /*
    bfs
    1. in a nested loop, find a 1 first
    */
    let cnt = 0;
    let row = grid.length;
    let col = grid[0].length;
    
    for(let i=0; i<row; i++){
        for(let j=0; j<col; j++){
            if(grid[i][j] === '1'){
                cnt++;
                dfs(i,j,grid)
            }
        }
    }
    
    
    function dfs(i,j,grid){
        if(i<0 || i>= grid.length || j<0 || j>= grid[0].length) return;
        
        if(grid[i][j] === "1"){
            grid[i][j] = "0"
        } else return;
        
        dfs(i+1, j, grid);
        dfs(i-1, j, grid);
        dfs(i,j+1, grid);
        dfs(i,j-1,grid);
    }
    return cnt
};