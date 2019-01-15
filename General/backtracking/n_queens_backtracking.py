class Solution():

    def n_queens(self):
        N = 4
        board = [[False]*N for i in range(0,N)]

        self.solve(board, 0, N)
        self.print_board(board)


    def solve(self, board, num_queens, N):

        if num_queens == N:
            return True

        open_positions = self.get_open_position(board, N)

        for position in open_positions:
            x = position[1]
            y = position[0]

            if self.is_safe(board, position):
                board[x][y] = True
                if self.solve(board, num_queens + 1, N):
                    return True
                else:
                    board[x][y] = False

        return False
        
    def get_open_position(self, board, N):
        open_positions = []
        for i in range(0, N):
            for j in range(0, N):
                if board[i][j] is False:
                    open_positions.append((i, j))
        
        return open_positions


    def is_safe(self, board, position):
        
        x = position[1]
        y = position[0]

        # Check left/right
        j = y
        for i in range(0, len(board)):
            if i != x and board[i][j] is True:
                return False

        # Check top/bottom
        i = x
        for j in range(0, len(board)):
            if j != y and board[i][j] is True:
                return False

        # Check from position to top left
        i = x
        j = y
        while i >= 0 and j >= 0:
            if board[i][j] is True:
                return False
            i -= 1
            j -= 1

        # Check from position to bottom right
        i = x
        j = y
        while i < len(board) and j < len(board):
            if board[i][j] is True:
                return False
            i += 1
            j += 1

        # Check from position to top right
        i = x
        j = y
        while i < len(board) and j >= 0:
            if board[i][j] is True:
                return False
            i += 1
            j -= 1

        # Check from position to bottom left
        i = x
        j = y
        while i >= 0 and j < len(board):
            if board[i][j] is True:
                return False
            i -= 1
            j += 1

        return True

    
    def print_board(self, board):
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
        for row in board]))

Solution().n_queens()




