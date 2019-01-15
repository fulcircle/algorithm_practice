# https://www.geeksforgeeks.org/the-knights-tour-problem-backtracking-1/

class Solution():

    def knights_tour(self):
        N = 5
        board = [[-1]*N for i in range(0,N)]

        # Since Knight is initially on first block
        board[0][0] = 0
        valid_moves = [(2, 1), (1, 2), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1)]
        self.solve_kt(board, N*N, (0, 0), 1, valid_moves)

        self.print_board(board)

    def solve_kt(self, board, board_size, current_coord, move_num, valid_moves):

        if move_num == board_size:
            return True

        for move in valid_moves:
            new_coord = (current_coord[0] + move[0], current_coord[1] + move[1])
            if self.is_safe(board, new_coord):

                board[new_coord[1]][new_coord[0]] = move_num

                if self.solve_kt(board, board_size, new_coord, move_num + 1, valid_moves):
                    return True
                else:
                    board[new_coord[1]][new_coord[0]] = -1
        
        return False

    
    def is_safe(self, board, coord):
        return coord[1] >= 0 and coord[1] < len(board) and coord[0] >= 0 and coord[0] < len(board[0]) and board[coord[1]][coord[0]] == -1

    def print_board(self, board):
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
        for row in board]))



Solution().knights_tour()