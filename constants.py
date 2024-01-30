import pygame

# Variables
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500
AMOUNT = 0

# Colors
GREY = (131, 139, 139)
BLACK = (0, 0, 0)
RED = (178, 34, 34)
YELLOW = (218, 165, 32)
GREEN = (34, 139, 34)
LIGHTRED = (255, 69, 0)
LIGHTYELLOW = (255, 255, 0)
LIGHTGREEN = (0, 255, 127)
LINEBORDER = (450, 0, 5, 500)

# Declaring the border's position of each player
player_1_border = pygame.Rect(0, 0, SCREEN_WIDTH // 2, SCREEN_HEIGHT)
player_2_border = pygame.Rect(SCREEN_WIDTH // 2, 0, SCREEN_WIDTH // 2, SCREEN_HEIGHT)

# Keyboard Inputs for each player
player_1_keys = {
    "UP": pygame.K_w,
    "DOWN": pygame.K_s,
    "LEFT": pygame.K_a,
    "RIGHT": pygame.K_d,
    "SHOOT": pygame.K_e
}

player_2_keys = {
    "UP": pygame.K_UP,
    "DOWN": pygame.K_DOWN,
    "LEFT": pygame.K_LEFT,
    "RIGHT": pygame.K_RIGHT,
    "SHOOT": pygame.K_RSHIFT
}

# Images
bullet_1 = pygame.image.load('assets/bullet.png')
bullet_1 = pygame.transform.scale(bullet_1, (60, 25))

bullet_2 = pygame.image.load('assets/bullet.png')
bullet_2 = pygame.transform.flip(bullet_2, True, False)
bullet_2 = pygame.transform.scale(bullet_2, (60, 25))

tank_1_image = pygame.image.load('assets/firsttank_image.png')
tank_1_image = pygame.transform.scale(tank_1_image, (150, 100))

tank_2_image = pygame.image.load('assets/secondtank_image.png')
tank_2_image = pygame.transform.scale(tank_2_image, (150, 100))
tank_2_image = pygame.transform.flip(tank_2_image, True, False)

heart1 = pygame.image.load('assets/lastheart.png')
heart1 = pygame.transform.scale(heart1, (150, 100))

heart2 = pygame.image.load('assets/healthbar3.png')
heart2 = pygame.transform.scale(heart2, (150, 100))

heart3 = pygame.image.load('assets/healthbar.png')
heart3 = pygame.transform.scale(heart3, (150, 100))