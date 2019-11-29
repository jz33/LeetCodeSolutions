'''
529. Minesweeper
https://leetcode.com/problems/minesweeper/

Update Minesweeper board based on current board and click point
'''
class Solution:
    def adjacentMines(self, board, click) -> int:
        ctr = 0
        for d in [(0,1),(1,1),(1,0),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1)]:
            i, j = click[0] + d[0], click[1] + d[1]
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == 'M':
                ctr += 1
        return ctr
               
    def updateNode(self, board, click) -> bool:
        '''
        Update a cell according to adjacent mines count.
        Return true if the cell is updated to blank.
        Only blank cells can recursively update neighbors.
        '''
        mc = self.adjacentMines(board, click)
        if mc == 0:
            board[click[0]][click[1]] = 'B'
            return True
        else:
            board[click[0]][click[1]] = str(mc)
            return False
        
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # Unreveal 'click'
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        
        if not self.updateNode(board, click):
            return board
   
        # BFS
        queue = collections.deque()
        queue.append(click)
        while queue:
            click = queue.popleft()
            
            # Unreveal node's neighbors
            for d in [(0,1),(1,1),(1,0),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1)]:
                i, j = click[0] + d[0], click[1] + d[1]
                if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == 'E':
                    if self.updateNode(board, (i,j)):
                        queue.append((i,j))
        
        return board
