GAME_WIN_WIDTH, GAME_WIN_HEIGHT = 1280, 720
BUTTON_WIN_WIDTH, BUTTON_WIN_HEIGHT = GAME_WIN_WIDTH, 50
BUTTON_HEIGHT = BUTTON_WIN_HEIGHT - 10
BUTTON_WIDTH = (BUTTON_WIN_WIDTH - 160) // 4
BUTTON_SPACING = 10
NODE_SPACING = 10
PLAYABLE_ROWS, PLAYABLE_COLUMNS = GAME_WIN_WIDTH // NODE_SPACING, GAME_WIN_HEIGHT // NODE_SPACING
TEXT_BUTTON_HEIGHT = 12

COLOURS = {
    "GRIDLINES" : (0, 0, 0),
    "TEXT" : (255, 255, 255),
    "BGCOLOUR" : (33, 53, 85),
    "BUTTON_LIGHT" : (216, 196, 182),
    "BUTTON_NORMAL" : (62, 88, 121),
    "NEUTRAL": (211, 211, 211),
    "VISITED": (255, 0, 0),
    "TO_BE_VISITED": (0, 255, 0),
    "START" : (255, 165, 0),
    "END" : (0, 206, 209),
    "BARRIER" : (0, 0, 0),
    "PATH" : (255, 255, 0)
}

STATES = {v:k for k, v in COLOURS.items()}
