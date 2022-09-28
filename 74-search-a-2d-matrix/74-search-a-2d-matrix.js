/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    //diagonal search. Time : o(m+n)
//     if(!matrix.length || !matrix[0].length) return false;
    
//     let row = 0;
//     let col = matrix[0].length-1;
    
//     while(col >= 0 && row <= matrix.length-1){
//         if(matrix[row][col] === target) return true;
//        else if(matrix[row][col] < target) row++;
//         else if(matrix[row][col] > target) col--;
//     }
//     return false
    
    //binary search. Time : O(mlgn)
    for(let i=0; i<matrix.length; i++){
        let start = 0, end = matrix[0].length-1;
        
        while(start <= end){
            let mid = Math.floor((start + end) / 2);
            if(matrix[i][mid] === target) return true;
            else if(matrix[i][mid] > target) end = mid-1;
            else if(matrix[i][mid] < target) start = mid+1
        }
    }
    return false
};