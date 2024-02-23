/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    let cnt = 0;
    let rows= grid.length;
    let cols = grid[0].length;
    
    for(let i=0; i<rows; i++){
        for(let j=0; j<cols; j++){
            if(grid[i][j] === '1'){
                dfs(grid, i,j);
                cnt++;
            }
        }
    }
    
    function dfs(grid, i,j){
        if(i <0 || j <0 || i >= grid.length || j >= grid[0].length) return;
        
            if(grid[i][j] === "1"){
            grid[i][j] = "0"
        } else return;
        
        
        dfs(grid, i+1, j);
        dfs(grid, i-1, j);
        dfs(grid, i, j+1);
        dfs(grid, i, j-1);
        
    }
    return cnt;
};