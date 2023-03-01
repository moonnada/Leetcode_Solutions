/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
  /*
  1. init 3 different sets for handling every case(row, col, 3*3)
  2. in a nested loop, init 3 current places for every case and test 3 different places
    2-1. if curRow is not equal to '.', and if curRow is in set already, return false, else put the cur value into set
    2-2..
    2-3..
  */
    
    
    
    for(let i=0; i<9; i++){
        let row = new Set();
    let col = new Set();
    let box = new Set();
        for(let j=0; j<9; j++){
            let curRow = board[i][j];
            let curCol = board[j][i];
            let curBox = board[3*Math.floor(i/3) + Math.floor(j/3)][3*(i%3)+ (j%3)];
            
            if(curRow !== "."){
                if(row.has(curRow)) return false;
                row.add(curRow)
            } 
            if(curCol !== "."){
                if(col.has(curCol)) return false;
                col.add(curCol)
            }
            if(curBox !== "."){
                if(box.has(curBox)) return false;
                box.add(curBox);
            }
        }
    }
    return true
};