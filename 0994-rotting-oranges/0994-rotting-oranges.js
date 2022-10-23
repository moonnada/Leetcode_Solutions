/**
 * @param {number[][]} grid
 * @return {number}
 */
var orangesRotting = function(grid) {
   /*
   bfs
   1. init values
   2. check edge cases
   3. traverse 2d arrs to find rotten orange and fresh oranges. 
    if find rotten, put its position into queue. 
    if find fresh, increment them
   4. while queue exists, get curVal from queue.shift()
    5. get queue's size and traverse surrouding areas to find rottens
    6. only visit surrounding areas if there is a fresh oranges\
        7. change cur orange to rotten
        7. push cur position into queue
        8. fresh--
    9. after all visit curQue' size, mins++
   */
    
    let mins = 0;
    let row = grid.length;
    let col = grid[0].length;
    let queue = [];
    let fresh = 0;
    
    for(let i=0; i<row; i++){
        for(let j=0; j<col; j++){
            if(grid[i][j] === 2){
                queue.push([i,j])
            } else if(grid[i][j] === 1) fresh++;
        }
    }
    
    while(queue.length){
      
        let size = queue.length;
        for(let i=0; i<size; i++){
            let [x,y] = queue.shift();
            if(x-1 >=0 && grid[x-1][y] === 1 ){
                queue.push([x-1,y]);
                fresh--;
                grid[x-1][y] = 2;
            }
            if(x+1 < row && grid[x+1][y] === 1 ){
                queue.push([x+1,y]);
                fresh--;
                grid[x+1][y] = 2;
            }
            if(y-1 >=0 && grid[x][y-1] === 1 ){
                queue.push([x,y-1]);
                fresh--;
                grid[x][y-1] = 2;
            }
            if(y+1 < col && grid[x][y+1] === 1 ){
                queue.push([x,y+1]);
                fresh--;
                grid[x][y+1] = 2;
            }
        }
        if(queue.length) mins++;
    }
    return fresh === 0 ? mins : -1
};