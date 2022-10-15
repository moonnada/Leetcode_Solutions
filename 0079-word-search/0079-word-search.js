/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function(board, word) {
    let x = board.length;
    let y = board[0].length;
    let wordLen = word.length;
    
    for(let i=0; i<x; i++){
        for(let j=0; j<y; j++){
            if(dfs(i,j,0)) return true; //word found
        }
    }
    
    function dfs(i,j,k){
        if(i>=0 && i < x && j>=0 && j < y && k < wordLen && board[i][j] == word[k]){
            if(k == word.length -1) return true;
            k = k+1; //next word
            
            let temp = board[i][j]; //for backtracking
            board[i][j] = "";
            
            let found = dfs(i+1,j,k) || dfs(i,j+1,k) || dfs(i-1,j,k) || dfs(i,j-1,k);
            board[i][j] = temp;
            return found;
        }
        return false;
    }
    return false
};