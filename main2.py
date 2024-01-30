import sys
from constants import *
from player import Player

# Initialize pygame
pygame.init()

# Screen setup
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('TANKS')


def game_over():
    running = True
    clock = pygame.time.Clock()

    # Declaring necessary fonts
    font1 = pygame.font.Font('freesansbold.ttf', 120)
    font2 = pygame.font.Font('freesansbold.ttf', 30)

    # Create the "Game Over" text rendered with a bigger font
    game_over_text = font1.render("Game Over", True, (0, 0, 0))
    game_over_text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))

    # Create the "Press any key to restart" text rendered with a smaller font
    restart_text = font2.render("Press space to restart", True, (0, 0, 0))
    restart_text_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 3) * 2))

    while running:
        # Handles the events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()

        # Displays the texts
        SCREEN.blit(game_over_text, game_over_text_rect)
        SCREEN.blit(restart_text, restart_text_rect)

        # Updates the display 60 times a second
        clock.tick(60)
        pygame.display.update()


def main():
    running = True
    clock = pygame.time.Clock()

    # Creating each player
    tank_1 = Player(SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2, tank_1_image, player_1_keys, player_1_border, True)
    tank_2 = Player((SCREEN_WIDTH // 3) * 2, SCREEN_HEIGHT // 2, tank_2_image, player_2_keys, player_2_border, False)

    # Declare each other as opponents
    tank_1.opponent = tank_2
    tank_2.opponent = tank_1

    while running:
        # Handles the events such as the keyboard presses
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Store the key presses into a variable
        input = pygame.key.get_pressed()

        # Fills the screen and draw line
        SCREEN.fill(GREY)
        pygame.draw.rect(SCREEN, BLACK, LINEBORDER)

        # Updates and displays both players
        tank_1.update(input)
        tank_2.update(input)
        tank_1.draw(SCREEN)
        tank_2.draw(SCREEN)

        # Checks if someone's health is less than one
        if tank_1.healthbar.hearts < 1 or tank_2.healthbar.hearts < 1:
            game_over()

        # Updates the display 60 times a second
        clock.tick(60)
        pygame.display.update()


main()
