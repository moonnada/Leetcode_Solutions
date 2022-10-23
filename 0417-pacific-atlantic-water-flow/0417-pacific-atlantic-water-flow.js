/**
 * @param {number[][]} heights
 * @return {number[][]}
 */
var pacificAtlantic = function(heights) {
    if(!heights.length) return [];
    
    let row = heights.length;
    let col = heights[0].length;
    
    let pacific = new Array(row).fill().map(() => Array(col).fill(false));
    let atlantic = new Array(row).fill().map(() => Array(col).fill(false));
    
    function dfs(r, c, cur, ocean){
        if(r<0 || r >= row || c < 0 || c >= col) return;
        if(heights[r][c] < cur) return;
        if(ocean[r][c]) return;
        ocean[r][c] = true;
        
        dfs(r+1,c,heights[r][c], ocean);
        dfs(r-1,c,heights[r][c], ocean);
        dfs(r,c+1,heights[r][c], ocean);
        dfs(r,c-1,heights[r][c], ocean);
    }
    
    for(let c=0; c<col; c++ ){
        dfs(0,c, Number.MIN_SAFE_INTEGER, pacific);
        dfs(row-1, c, Number.MIN_SAFE_INTEGER, atlantic);
    }
    
    for(let r=0; r<row; r++){
        dfs(r,0,Number.MIN_SAFE_INTEGER,pacific);
        dfs(r,col-1, Number.MIN_SAFE_INTEGER, atlantic);
    }
    
    let ans = [];
    for(let i=0; i<row; i++){
        for(let j=0; j<col; j++){
            if(atlantic[i][j] && pacific[i][j]) ans.push([i,j])
        }
    }
    
    return ans;
};