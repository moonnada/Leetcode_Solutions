/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solve = function(board) {
   /*
   DFS
   1. traverse 2d arrs to find 'x's in boards
    2. if find 'x' in boards, then deep inside by using a helper func
    
    3. in a helper func, check edge cases first.
        4. curPostion is marked to 'visited'
        5. visit 4 different ways
    
    6. traverse 2d arr to change chars.
        7. if position is marked as 'visited', then change to 'x', if position is marked as 'o', changed to 'x'
   */
    
    let row = board.length;
    let col = board[0].length;
    
    for(let i=0; i<row; i++){
        for(let j=0; j<col; j++){
            if(board[i][j] === 'O' && (i=== 0 || j === 0 || i=== row-1 || j === col-1)) dfs(i,j);
        }
    }
    
    function dfs(i,j){
        if(i < 0 || i>= row || j < 0 || j>= col || board[i][j] !== 'O') return;
        
        board[i][j] = 'visited';
        dfs(i-1,j);
        dfs(i+1, j);
        dfs(i,j-1);
        dfs(i,j+1);
    }
    
    for(let i=0; i<row; i++){
        for(let j=0; j<col; j++){
            if(board[i][j] === 'visited'){
                board[i][j] = 'O';
            } else if( board[i][j] === 'O'){
                board[i][j] = 'X'
            }
        }
    }
    
    return board;
};