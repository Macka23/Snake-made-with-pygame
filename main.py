import pygame
from pygame.locals import *
from random import randrange

# Initializing game
pygame.init()
screen_surface = pygame.display.set_mode((480, 600))
clock = pygame.time.Clock()

# Colors
black = 0, 0, 0
white = 255, 255, 255
green = 154, 205, 50
red = 255, 0, 0
yellow = 255, 255, 0
pink = 255, 153, 153
blue = 0, 0, 255

# Background surface
background = pygame.Surface(screen_surface.get_size())
background.fill(black)

# Surface where snake can move over every sprite of the screen
surfsk = pygame.Surface(screen_surface.get_size())
surfsk.set_colorkey((0, 0, 0))


# check if player lost
def check_4loose(all_positions_player, sk_he_x, sk_he_y, points):
    for x in (n + 1 for n in range(points)):
        if sk_he_x == all_positions_player[len(all_positions_headsk) - (2 * x) - 2] and \
                sk_he_y == all_positions_player[len(all_positions_headsk) - (2 * x) - 1]:
            return False

        if sk_he_x < -10 or sk_he_x > 480 or sk_he_y < -10 or sk_he_y > 600:
            return False

    return True


while True:
    headsk_x, headsk_y = 50, 50
    move_x, move_y = 0, 10
    vertical_var = 1
    horizontal_var = 0
    all_positions_headsk = [0, 0]
    score = 3
    appel_posx, appel_posy = randrange(0, 470, 10), randrange(0, 590, 10)
    background.fill(black)

    # Creating the first appel
    sprite_appel = pygame.Rect(appel_posx, appel_posy, 10, 10)
    pygame.draw.rect(background, red, sprite_appel)

    # Start menu loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()

        key = pygame.key.get_pressed()  # Pygame module for inputs
        if key[K_RETURN]:
            break

        if key[K_ESCAPE]:
            quit()

        snake_font = pygame.font.Font('Terasong-mLZ3a.ttf', 48)
        font = pygame.font.Font('Terasong-mLZ3a.ttf', 24)
        text = font.render('Press Enter to start the game', True, green)
        text2 = font.render('Press Echap to quit the game', True, red)
        text3 = snake_font.render('snake', True, yellow)
        screen_surface.blit(text, (50, 300))
        screen_surface.blit(text2, (50, 500))
        screen_surface.blit(text3, (140, 100))
        pygame.display.flip()

    # Game loop
    while True:
        # If the player wants to quit, no error will be shown
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()

        key = pygame.key.get_pressed()  # Pygame module for inputs

        surfsk.fill((0, 0, 0, 0))  # Erase the old square (only hiding it with a black screen)

        if key[K_UP] and vertical_var != 1:
            move_y = -10
            move_x = 0
            vertical_var = 1
            horizontal_var = 0

        if key[K_DOWN] and vertical_var != 1:
            move_y = 10
            move_x = 0
            vertical_var = 1
            horizontal_var = 0

        if key[K_RIGHT] and horizontal_var != 1:
            move_x = 10
            move_y = 0
            horizontal_var = 1
            vertical_var = 0

        if key[K_LEFT] and horizontal_var != 1:
            move_x = -10
            move_y = 0
            horizontal_var = 1
            vertical_var = 0

        all_positions_headsk.append(headsk_x)
        all_positions_headsk.append(headsk_y)

        # Drawing the square each loop + sprite of it
        spritesk = pygame.Rect(headsk_x, headsk_y, 10, 10)
        pygame.draw.rect(surfsk, yellow, spritesk)

        # Creating squares that follow the headsk
        for i in (n + 1 for n in range(score)):
            sprite_tail_sk = pygame.Rect(all_positions_headsk[len(all_positions_headsk) - (2 * i) - 2],
                                         all_positions_headsk[len(all_positions_headsk) - (2 * i) - 1], 10, 10)
            pygame.draw.rect(surfsk, yellow, sprite_tail_sk)

        headsk_x += move_x
        headsk_y += move_y

        # Create a red appel randomly on the screen
        if headsk_x == appel_posx and headsk_y == appel_posy:
            appel_posx = randrange(0, 470, 10)
            appel_posy = randrange(0, 590, 10)
            background.fill(black)
            score += 1
            sprite_appel = pygame.Rect(appel_posx, appel_posy, 10, 10)
            pygame.draw.rect(background, red, sprite_appel)

        if check_4loose(all_positions_headsk, headsk_x, headsk_y, score) is not True:
            break

        screen_surface.blit(background, (0, 0))
        screen_surface.blit(surfsk, (0, 0))
        clock.tick(30)  # Setting game speed (FPS)
        pygame.display.flip()
