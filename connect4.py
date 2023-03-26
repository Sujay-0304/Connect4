
# hiiii how are ourlashflhasdf
BOARD_COLS = 7
BOARD_ROWS = 6
class Board():
    def __init__(self):
        self.board = [list(' '*BOARD_COLS) for _ in range(BOARD_ROWS)]
        self.turns = 0
        self.last_move = [-1, -1]

    def print_board(self):
        for r in range(BOARD_COLS):
            print(f" {r+1}", end="")
        print()
        for r in range(BOARD_ROWS):
            print('|', end="")
            for c in range(BOARD_COLS):
                print(f"{self.board[r][c]}|", end="")
            print("\n")
        print(f"{'-' * 24}")

    def which_turn(self):
        players = ['X', 'O']
        return players[self.turns % 2]
    
    def in_bounds(self, r, c):
        return (r >= 0 and r < BOARD_ROWS and c >= 0 and c < BOARD_COLS)

    def turn(self, column):
        for i in range(BOARD_ROWS-1, -1, -1):
            if self.board[i][column] == ' ':
                self.board[i][column] = self.which_turn()
                self.last_move = [i, column]
                self.turns += 1
                return True
        return False

    def check_winner(self):
        last_row = self.last_move[0]
        last_col = self.last_move[1]
        last_letter = self.board[last_row][last_col]
        ######################
        def dfs(x,y,count,horizontalleft,vertical,horizontalright,diaupright,diaupleft,diabotright,diabotleft):
            if count >= 4:
                self.print_board()
                print(f"{last_letter}is the winner")
                quit()
            if self.in_bounds(x,y) == 0:
                return
            if self.board[x][y] == last_letter:count += 1
            else: return
            if horizontalleft:
                dfs(x+1,y,count,1,0,0,0,0,0,0)
            if vertical:
                dfs(x,y+1,count,0,1,0,0,0,0,0)
            if horizontalright:
                dfs(x,y-1,count,0,0,1,0,0,0,0)
            if diaupright:
                dfs(x-1,y+1,count,0,0,0,1,0,0,0)
            if diaupleft:
                dfs(x-1,y-1,count,0,0,0,0,1,0,0)
            if diabotright:
                dfs(x+1,y+1,count,0,0,0,0,0,1,0)
            if diabotleft:
                dfs(x+1,y-1,count,0,0,0,0,0,0,1)
            # dfs(x,y+1,count,horizontal,vertical)
        dfs(last_row,last_col,0,1,0,0,0,0,0,0)
        dfs(last_row,last_col,0,0,1,0,0,0,0,0)
        dfs(last_row,last_col,0,0,0,1,0,0,0,0)
        dfs(last_row, last_col, 0, 0, 0, 0, 1, 0, 0, 0)
        dfs(last_row, last_col, 0, 0, 0, 0, 0, 1, 0, 0)
        dfs(last_row, last_col, 0, 0, 0, 0, 0, 0, 1, 0)
        dfs(last_row, last_col, 0, 0, 0, 0, 0, 0, 0, 1)
        return False

def play():
    game = Board()
    game_over = False
    while not game_over:
        game.print_board()
        valid_move = False
        while not valid_move:
            user_move = input(f"{game.which_turn()}'s Turn - pick a column (1-{BOARD_COLS}): ")
            try:
                valid_move = game.turn(int(user_move)-1)
            except:
                print(f"Please choose a number between 1 and {BOARD_COLS}")
        game_over = game.check_winner()
        if not any(' ' in x for x in game.board):
            print("The game is a draw..")
            quit()
play()
