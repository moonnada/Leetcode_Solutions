/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {

    //binary search. Time : O(m lg n)
//     for(let i=0; i<matrix.length; i++){
//         let start = 0, end = matrix[0].length-1;
        
//         while(start <= end){
//             let mid = Math.floor((start + end) / 2);
//             if(matrix[i][mid] === target) return true;
//             else if(matrix[i][mid] > target) end = mid-1;
//             else if(matrix[i][mid] < target) start = mid+1
//         }
//     }
//     return false
    
    //binary search. complete matrix. Time : O(lg mn)
    // let start = 0, end = (matrix.length * matrix[0].length) -1;
    // while(start <= end){
    //     let mid = Math.floor((start + end) / 2);
    //     let midNum = matrix[Math.floor(mid / matrix[0].length)][mid % matrix[0].length];
    //     if(midNum === target) return true;
    //     else if(midNum > target) end = mid-1;
    //     else if(midNum < target) start = mid+1;
    // }
    // return false
    
    for(let i=0; i<matrix.length; i++){
        let start = 0, end = matrix[0].length-1;
        
        while(start <= end){
            let mid = Math.floor((start + end) /2);
            if(matrix[i][mid] === target) return true;
            if(matrix[i][mid] > target) end = mid-1;
            else start = mid + 1
        }
    }
    return false
};