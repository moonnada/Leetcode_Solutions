/**
 * @param {number[][]} grid
 * @return {number}
 */
var orangesRotting = function(grid) {
    let row = grid.length;
    let col = grid[0].length;
    let queue = [];
    let fresh = 0;
    let mins = 0;
    
    for(let i=0; i<row; i++){
        for(let j=0; j<col; j++){
            if(grid[i][j] === 2){
                queue.push([i,j]);
            }
            if(grid[i][j] === 1) fresh++;
        }
    }
    
    while(queue.length){
        let size = queue.length;
        
        for(let i=0; i<size; i++){
            let [x,y] = queue.shift();
            
            if(x-1 >= 0 && grid[x-1][y] === 1){
                grid[x-1][y] = 2;
                fresh--;
                queue.push([x-1,y]);
            }
            
            if(x+1 < row && grid[x+1][y] === 1){
                grid[x+1][y] = 2;
                fresh--;
                queue.push([x+1,y])
            }
            
            if(y+1 < col && grid[x][y+1] === 1){
                grid[x][y+1] = 2;
                fresh--;
                queue.push([x,y+1])
            }
            
            if(y-1 >=0 && grid[x][y-1] === 1){
                grid[x][y-1] = 2;
                fresh--;
                queue.push([x,y-1])
            }     
        }
        if(queue.length > 0) mins++;
    }
     return fresh === 0 ? mins : -1
};