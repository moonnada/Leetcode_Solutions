/**
 * @param {number[][]} rooms
 * @return {void} Do not return anything, modify rooms in-place instead.
 */
var wallsAndGates = function(rooms) {
    //BFS
//     if(!rooms.length) return;
    
//     const EMPTY = 2147483647,
//           GATE = 0,
//           DIR = [
//               [1,0], //top row
//               [-1,0], //bottom row
//               [0,1], //right col
//               [0,-1] //left col
//           ];
//     let queue = [];
//     let row = rooms.length;
//     let col = rooms[0].length;
    
//     for(let i=0; i<row; i++){
//         for(let j=0; j<col; j++){
//             if(rooms[i][j] == GATE) {
//                 queue.push([i,j])
//             }
//         }
//     }
    
//     while(queue.length){
//         const curr = queue.shift();
//         let curRow = curr[0], curCol = curr[1];
        
//         for(let dir of DIR){
//             let r = curRow + dir[0];
//             let c = curCol + dir[1];
            
//             if(r<0 || c<0 ||r >=row || c >= col || rooms[r][c] != EMPTY) continue;
            
//             rooms[r][c] = rooms[curRow][curCol] + 1;
//             queue.push([r,c])
//         }
//     }
    
    const n = rooms.length;
    const m = rooms[0].length;
    const result = [];
    
   
const isAvailable = (rooms, n, m, i, j, path, visited) => {
    return i >= 0 && i < n && j >= 0 && j < m && rooms[i][j] > path;
};
const goFor = (rooms, n, m, i, j, path) => {
    if (!isAvailable(rooms, n, m, i, j, path)) return;
    
    rooms[i][j] = Math.min(path, rooms[i][j]);
    
    // Going top
    goFor(rooms, n, m, i - 1, j, path + 1);
    
    // Going right
    goFor(rooms, n, m, i, j + 1, path + 1);
    
    // Going down
    goFor(rooms, n, m, i + 1, j, path + 1);
    
    // Going left
    goFor(rooms, n, m, i, j - 1, path + 1);
};
     for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (rooms[i][j] === 0) {
                goFor(rooms, n, m, i - 1, j, 1);
                goFor(rooms, n, m, i, j + 1, 1);
                goFor(rooms, n, m, i + 1, j, 1);
                goFor(rooms, n, m, i, j - 1, 1);
            }
        }
    }
    
};