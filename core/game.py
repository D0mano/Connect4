from constante import *


class Game:
    def __init__(self):
        self.board = [[0 for x in range(7)] for y in range(6)]
        self.turn = PLAYER_1
        self.selected_col = 3

        # Command keys
        self.left_arrow = False
        self.right_arrow = False
        self.enter = False
        self.escape = False
        self.space = False
        self.mouse_motions = False
        self.mouse_pos = (0, 0)

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
            self.put_token(self.selected_col,self.turn)
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
                    return True
        return False

