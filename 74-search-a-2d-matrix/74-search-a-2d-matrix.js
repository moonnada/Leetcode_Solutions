/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    //diagonal search. Time : o(m+n)
    if(!matrix.length || !matrix[0].length) return false;
    
    let row = 0;
    let col = matrix[0].length-1;
    
    while(col >= 0 && row <= matrix.length-1){
        if(matrix[row][col] === target) return true;
       else if(matrix[row][col] < target) row++;
        else if(matrix[row][col] > target) col--;
    }
    return false
};