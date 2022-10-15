/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function(board, word) {
    /*
    DFS. backtracking
    1. init row and col and visited
    2. traverse 2d arr and if we find the first letter and visit by using a helper func. return true
    3. in a helper func (i,j,idx, word, board)
    3.1) if idx = word.length, return true // reaching the final word
    3.2) check edge cases
    3.3) mark current place as visited
    3.4) visit recursively horizontal and vertical ways
    */
    
    let row = board.length; 
    let col = board[0].length;
    for(let i=0; i<row; i++){
        for(let j=0; j<col; j++){
            if(word.charAt(0) === board[i][j] && dfs(i,j, 0, word, board)) return true;
        }
    }
    
    return false;
    
    function dfs(i,j, idx, word, board){
        if(idx === word.length) return true;
        if(i<0 || i>= board.length || j < 0 || j>= board[i].length || word.charAt(idx) !== board[i][j]) return false;
        
        //choose
        let tmp = board[i][j];
        board[i][j] = "*";
        
        //explore
        if( dfs(i+1, j, idx+1, word,board) ||
            dfs(i-1, j, idx+1, word, board) ||
            dfs(i, j+1, idx+1, word, board) ||
            dfs(i, j-1, idx+1, word, board)
          ) return true;
        
        //unchoose
        board[i][j] = tmp;
        return false
    }
};