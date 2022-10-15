/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    let cnt = 0;
    for(let i=0; i<grid.length; i++){
        for(let j=0; j<grid[0].length; j++){
            if(grid[i][j] === "1"){
                cnt++;
                dfs(i,j, grid)
            }
        }
    }
    return cnt
    
    function dfs(i,j, grid){
        if(i<0 || i>=grid.length || j <0 || j>= grid[0].length) return;
        
        if(grid[i][j] === "1"){
            grid[i][j] = "0";
        } else return;
        
        dfs(i+1, j, grid);
        dfs(i-1, j, grid);
        dfs(i, j+1, grid);
        dfs(i, j-1, grid)
    }
};