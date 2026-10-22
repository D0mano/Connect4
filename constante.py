# === DIMENSIONS AND DISPLAY ===
ROWS = 6
COLS = 7

SQUARE_SIZE = 100
PADDING = 10
RADIUS = int(SQUARE_SIZE / 2 - PADDING)

BOARD_WIDTH = COLS * SQUARE_SIZE
BOARD_HEIGHT = ROWS * SQUARE_SIZE

# Top area to select column before dropping
EXTRA_TOP_SPACE = SQUARE_SIZE 
WINDOW_WIDTH = BOARD_WIDTH
WINDOW_HEIGHT = BOARD_HEIGHT + EXTRA_TOP_SPACE

# Offset if you decide to center the board in a larger window later
OFFSET_X = 0
OFFSET_Y = EXTRA_TOP_SPACE

# === COLORS (RGB format) ===
# Board colors
BOARD_COLOR = (0, 0, 255)         # Blue
EMPTY_COLOR = (0, 0, 0)           # Black

# Player colors
PLAYER_1_COLOR = (255, 0, 0)      # Red
PLAYER_2_COLOR = (255, 255, 0)    # Yellow

# UI Colors
BACKGROUND_COLOR = (48, 46, 43)   # Dark gray
HIGHLIGHT_COLOR = (255, 255, 255, 100) # White transparent for hover
WINNING_LINE_COLOR = (0, 255, 0)  # Green

# Text colors
TEXT_COLOR_WHITE = (255, 255, 255)
TEXT_COLOR_BLACK = (0, 0, 0)

# === PLAYER AND PIECE IDENTIFIERS ===
EMPTY = 0
PLAYER_1 = 1
PLAYER_2 = -1

# === GAME STATES ===
GAME_IN_PROGRESS = 0
PLAYER_1_WINS = 1
PLAYER_2_WINS = 2
DRAW = 3

# === GAME CONFIGURATIONS ===
FPS = 60

# Font sizes
SIZE_MAIN_FONT = 60
SIZE_INTERFACE_FONT = 30

# === WINNING DIRECTIONS (Row delta, Col delta) ===
# Used to check for 4-in-a-row (Horizontal, Vertical, Diagonals)
DIRECTIONS = [
    (0, 1),   # Horizontal (right)
    (1, 0),   # Vertical (down)
    (1, 1),   # Diagonal (down-right)
    (1, -1)   # Diagonal (down-left)
]

# === INITIAL BOARD STATE ===
INITIAL_BOARD = [
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]
]

# === TEST / DEBUG BOARDS ===
BOARD_ALMOST_WIN = [
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [PLAYER_2, PLAYER_2, PLAYER_2, EMPTY, EMPTY, EMPTY, EMPTY],
    [PLAYER_1, PLAYER_1, PLAYER_1, EMPTY, EMPTY, EMPTY, EMPTY]
]