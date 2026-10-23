from constante import *


class Game:
    def __init__(self):
        self.board = [[0 for x in range(7)] for y in range(6)]
        self.turn = PLAYER_1
        self.selected_col = 3

        self.last_token_pos = None
        self.game_winners_tokens = []

        # Command keys
        self.left_arrow = False
        self.right_arrow = False
        self.enter = False
        self.escape = False
        self.space = False
        self.mouse_motions = False
        self.mouse_pos = (0, 0)

        # Game State
        self.game_over = False

    def switch_turn(self):
        self.turn = - self.turn


    def mouse_set_selected_row(self,pos):
        pos_y = pos[0] - OFFSET_X
        selected_row = pos_y // SQUARE_SIZE
        self.selected_col = selected_row


    def update_game(self):
        if self.right_arrow:
            self.selected_col += 1 if self.selected_col < 6 else 0
            self.right_arrow = False
        elif self.left_arrow:
            self.selected_col -= 1 if self.selected_col > 0 else 0
            self.left_arrow = False
        elif self.space:
            if self.put_token(self.selected_col,self.turn):
                if self.check_win():
                    self.game_over = True
                    print('GAME OVER')
                    if self.turn == PLAYER_1:
                        print('PLAYER 1 WINS')
                    else:
                        print('PLAYER 2 WINS')
            self.space = False
            self.enter = False
            self.switch_turn()
        elif self.escape:
            pass
        if self.mouse_motions:
            self.mouse_set_selected_row(self.mouse_pos)


    def put_token(self,selected_col,turn):
        for row in range(len(self.board)-1,-1,-1):
            for col in range(len(self.board[row])):
                token = self.board[row][col]
                if token == EMPTY and col == selected_col:
                    self.board[row][col] = turn
                    self.last_token_pos = (row,col)
                    return True
        return False


    def check_win(self):
        r,c = self.last_token_pos
        last_token = self.board[r][c]


        for dr,dc in DIRECTIONS:
            wining_positions = [(r,c)]

            for i in range(1,4):
                nr ,nc = r + (dr * i), c + (dc * i)
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    if self.board[nr][nc] == last_token:
                        wining_positions.append((nr,nc))
                    else:
                        break

            for j in range(1,4):
                nr , nc = r - (dr * j), c - (dc * j)
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    if self.board[nr][nc] == last_token:
                        wining_positions.append((nr,nc))
                    else:
                        break
            if len(wining_positions) >= 4:
                self.game_winners_tokens = wining_positions
                return True

        return False

