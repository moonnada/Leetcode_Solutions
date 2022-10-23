/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solve = function(board) {
    //check border lines first.
    for(let i = 0; i < board.length; i++) {
        for(let j = 0; j < board[0].length; j++) {
            if(board[i][j] === 'O' && (i === 0 || j === 0 || i === board.length - 1 || j === board[0].length - 1)) dfs(i, j);
        }
    }

    for(let i = 0; i < board.length; i++) {
        for(let j = 0; j < board[0].length; j++) {
            if(board[i][j] === 'Visited') {
                board[i][j] = 'O';
            } else  {
                board[i][j] = 'X';
            }
        }    
    }
    //mark 'visited when 'O' is on borders. if the 'O' is connected to middle point, then the place is useless point.
    function dfs(i, j) {
        if(i < 0 || i >= board.length || j < 0 || j >= board[i].length || board[i][j] === 'Visited' || board[i][j] === 'X') return
        
        board[i][j] = 'Visited';
        dfs(i + 1, j);
        dfs(i - 1, j);
        dfs(i, j + 1);
        dfs(i, j - 1);
        
        return;
    }
};