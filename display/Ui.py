import pygame
from core.game import Game
from constante import*
import display.functions
from display.functions import create_gradient_circle

pygame.init()

class Ui:
    DEFAULT_SCREEN_WIDTH = 800
    DEFAULT_SCREEN_HEIGHT = 600

    # STATES

    def __init__(self):
        self.screen_width = WINDOW_WIDTH
        self.screen_height = WINDOW_HEIGHT
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()

        self.game = Game()
        self.running = True

        #STATES
        self.in_menu = True
        self.in_game = False
        self.in_pause = False

    def run(self):
        while self.running:
            self.handle_events()
            self.game.update_game()
            self.draw()


    def draw(self):
        if self.in_menu:
            self.draw_main_menu()
        elif self.in_game:
            self.draw_game()


    def handle_events(self):
        for event in pygame.event.get():
            if self.in_menu:
                self.handle_main_menu_events(event)
            if self.in_game:
                self.handle_game_event(event)


    def draw_main_menu(self):
        circle = create_gradient_circle(300, (0, 0, 139), (0, 0, 0))
        circle_rect = circle.get_rect(center=(self.screen_width / 2, self.screen_height / 2))
        
        self.screen.fill((0, 0, 0))
        self.screen.blit(circle, circle_rect)
        pygame.display.flip()


    def handle_main_menu_events(self, event):
        if event.type == pygame.QUIT:
            self.running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print("In game")
                self.in_menu = False
                self.in_game = True


    def draw_game(self):

        self.screen.fill((0, 0, 0))
        self.draw_board()

        if self.game.game_over:
            self.highlight_winning_tokens()
        pygame.display.flip()


    def handle_game_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("In menu")
                self.in_game = False
                self.in_menu = True
            if event.key == pygame.K_LEFT or event.key == pygame.K_q:
                self.game.left_arrow = True
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.game.right_arrow = True
            if event.key == pygame.K_RETURN:
                self.game.enter = True
            if event.key == pygame.K_SPACE:
                self.game.space = True
        if event.type == pygame.MOUSEMOTION:
            self.game.mouse_motions = True
            self.game.mouse_pos = event.pos
        else:
            self.game.mouse_motions = False


    def draw_board(self):

        for y in range(len(self.game.board)):
            for x in range(len(self.game.board[y])):
                # 1. Calculer la position (coin supérieur gauche) de la case en cours
                pos_x = OFFSET_X + (x * SQUARE_SIZE)
                pos_y = OFFSET_Y + (y * SQUARE_SIZE)

                # 2. Dessiner le bloc bleu du plateau
                pygame.draw.rect(self.screen, BOARD_COLOR, (pos_x, pos_y, SQUARE_SIZE, SQUARE_SIZE))

                # 3. Déterminer ce qu'il y a dans la case
                case = self.game.board[y][x]
                if case == EMPTY:
                    color = EMPTY_COLOR
                elif case == PLAYER_1:
                    color = PLAYER_1_COLOR
                elif case == PLAYER_2:
                    color = PLAYER_2_COLOR

                # 4. Calculer le centre de la case pour y dessiner le jeton ou le trou
                center_x = pos_x + (SQUARE_SIZE // 2)
                center_y = pos_y + (SQUARE_SIZE // 2)

                pygame.draw.circle(self.screen, color, (center_x, center_y), RADIUS)

        selected_row_center = self.game.selected_col * SQUARE_SIZE + SQUARE_SIZE / 2

        points =[(selected_row_center-(SQUARE_SIZE/4),OFFSET_Y - SQUARE_SIZE),
                 (selected_row_center+(SQUARE_SIZE/4),OFFSET_Y - SQUARE_SIZE),
                  (selected_row_center,SQUARE_SIZE/2)]
        pygame.draw.polygon(self.screen,(255,255,255),points)


    def highlight_winning_tokens(self):
        self.game.game_winners_tokens.sort()
        first_r,first_c = self.game.game_winners_tokens[0]
        last_r,last_c = self.game.game_winners_tokens[-1]

        first_pos = (OFFSET_X + first_c * SQUARE_SIZE + SQUARE_SIZE // 2, OFFSET_Y + first_r * SQUARE_SIZE + SQUARE_SIZE // 2)
        last_pos = (OFFSET_X + last_c * SQUARE_SIZE + SQUARE_SIZE // 2 , OFFSET_Y + last_r * SQUARE_SIZE + SQUARE_SIZE // 2)


        pygame.draw.line(self.screen,WINNING_LINE_COLOR,first_pos,last_pos,3)







