/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    /*
    backtracking dfs
    1. check edge case(empty..)
    2. traverse 2d grid and if find a land, then cnt++ and by using a helper func, deep dive inside.
    3. in a helper func, check out of range first. and then if cur postion is land, change the cur position to 0 to avoid recounting 
    4. visit 4 different ways by using recursion
    */
    
    let cnt = 0;
    let row = grid.length;
    let col = grid[0].length;
    
    // if(!grid[row][col]) return cnt;
    
    for(let i=0; i<row; i++){
        for(let j=0; j<col; j++){
            if(grid[i][j] === "1"){
                cnt++;
                dfs(i,j,grid);
            }
        }
    }
    
    function dfs(i,j,grid){
        if(i<0 || i>=grid.length || j<0 || j>=grid[0].length) return;
        
        if(grid[i][j] === "1"){
            grid[i][j] = "0";
        }else return;
        
        
        dfs(i+1,j,grid);
        dfs(i-1, j,grid);
        dfs(i,j+1,grid);
        dfs(i,j-1,grid);
    }
    return cnt
};