/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxAreaOfIsland = function(grid) {
    //dfs
    /*
    1. traverse the grid
        2. if find island, go inside by using a helper func
    3. in a helper func, first of all, check all edge cases
        4. if cur position is island, then trying to visit all 4 different ways to find island.
        5. if next position is island, cnt++
    */
    
    let maxLand = 0;
    let row = grid.length;
    let col = grid[0].length;
    
    for(let i=0; i<row; i++){
        for(let j=0; j<col; j++){
           if(grid[i][j]){
               maxLand = Math.max(maxLand, trav(i,j,grid))
           }
        }
    }
    return maxLand;
    
    
   function trav(i,j,grid) {
        if(i < 0 || i>= grid.length || j < 0 || j >= grid[0].length || grid[i][j] == 0) return 0;
        
       grid[i][j] = 0;
        return (1+ trav(i-1,j,grid) + trav(i+1,j,grid) + trav(i,j-1,grid) + trav(i,j+1,grid) )
    }
    
    

};