from constante import PLAYER_1


class Game:
    def __init__(self):
        self.board = [[0 for x in range(7)] for y in range(6)]
        self.turn = PLAYER_1
        self.selected_row = 3

    def switch_turn(self):
        self.turn = - self.turn

    def update_game(self):
        pass

