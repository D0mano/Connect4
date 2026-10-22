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
            if self.in_menu:
                self.draw_main_menu()
            elif self.in_game:
                self.draw_game()

            for event in pygame.event.get():
                if self.in_menu:
                    self.handle_main_menu_events(event)
                if self.in_game:
                    self.handle_game_in_progress_event(event)



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
        circle = create_gradient_circle(300, (0, 0, 139), (0, 0, 0))
        circle_rect = circle.get_rect(center=(self.screen_width / 2, self.screen_height / 2))

        self.screen.fill((0, 0, 0))
        self.screen.blit(circle, circle_rect)

        self.draw_board()
        pygame.display.flip()

    def handle_game_in_progress_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("In menu")
                self.in_game = False
                self.in_menu = True
            if event.key == pygame.K_LEFT:
                self.game.selected_row -= 1 if self.game.selected_row > 0 else 0
            if event.key == pygame.K_RIGHT:
                self.game.selected_row += 1 if self.game.selected_row < 6 else 0
        if event.type == pygame.MOUSEMOTION:
            self.mouse_set_selected_row(event)

    def mouse_set_selected_row(self,event):
        pos_y = event.pos[0] - OFFSET_X
        selected_row = pos_y // SQUARE_SIZE
        self.game.selected_row = selected_row

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

        selected_row_center = self.game.selected_row * SQUARE_SIZE + SQUARE_SIZE/2

        points =[(selected_row_center-(SQUARE_SIZE/4),OFFSET_Y - SQUARE_SIZE),
                 (selected_row_center+(SQUARE_SIZE/4),OFFSET_Y - SQUARE_SIZE),
                  (selected_row_center,SQUARE_SIZE/2)]
        pygame.draw.polygon(self.screen,(255,255,255),points)







