# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

""" OBJ : Create a labyrinth game
    MacGyver must to leave the labyrinth with three objects

Attribute letters in labyrinth.txt file

D : Start position
S : End position
M : The wall
C : The way
W : Wrong way"""

import pygame
from game import Game

pygame.init()

# generate window's game
pygame.display.set_caption("labyrinth Game")
resolution = [645, 645]
screen = pygame.display.set_mode([resolution[0], resolution[1]])
coeff_screen = [15]
scall_screen = [resolution[0] // coeff_screen[0], resolution[1] // coeff_screen[0]]

# Import Background's picture
background = pygame.image.load('macgyver_ressources/ressource/RDL_FDC.jpeg')

# Import Wall Labyrinth
wall = pygame.image.load('macgyver_ressources/ressource/bricks-small.png')

# Import Way Labyrinth
way = pygame.image.load('macgyver_ressources/ressource/tiles-medium.png')

# Import Guardian
Guardian = pygame.image.load('macgyver_ressources/ressource/Gardien.png')

# Import Lose picture
lose = pygame.image.load('macgyver_ressources/ressource/loser.PNG')

# Import Victory picture
Victory = pygame.image.load('macgyver_ressources/ressource/victoire.JPG')

from find import Find

check_gard = Find()
for GUARD in check_gard.search('S'):
    GUARD[0] = GUARD[0] * scall_screen[0]
    GUARD[1] = GUARD[1] * scall_screen[1]

# Import wall position
check_wall = Find()

# Import way position
check_way = Find()

# Load Game
game = Game()

running = True

# repeat for test

while running:

    # Background position
    screen.blit(background, (-450, -100))

    # Wall picture
    for WALL in check_wall.search('M'):
        WALL[0] = WALL[0] * scall_screen[0]
        WALL[1] = WALL[1] * scall_screen[1]
        screen.blit(wall, ((WALL[0]), (WALL[1])))

    # Way picture
    for WAY in check_way.search('C'):
        WAY[0] = WAY[0] * scall_screen[0]
        WAY[1] = WAY[1] * scall_screen[1]
        screen.blit(way, ((WAY[0]), (WAY[1])))
    for WAY in check_way.search('D'):
        WAY[0] = WAY[0] * scall_screen[0]
        WAY[1] = WAY[1] * scall_screen[1]
        screen.blit(way, ((WAY[0]), (WAY[1])))
    for WAY in check_way.search('S'):
        WAY[0] = WAY[0] * scall_screen[0]
        WAY[1] = WAY[1] * scall_screen[1]
        screen.blit(way, ((WAY[0]), (WAY[1])))

    # Guardian position
    screen.blit(Guardian, ((GUARD[0]), (GUARD[1])))

    # Player's picture
    screen.blit(game.player.image, game.player.rect)

    # MAJ screen
    pygame.display.flip()

    # player close the window
    for event in pygame.event.get():
        # if event closed the window
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("See You Soon")
        elif event.type == pygame.KEYDOWN:
            # what button was pushed
            if event.key == pygame.K_RIGHT:
                game.player.move_right()
                for WALL in check_wall.search('M'):
                    WALL[0] = WALL[0] * scall_screen[0]
                    WALL[1] = WALL[1] * scall_screen[1]
                    Check_P = [game.player.rect.x, game.player.rect.y]
                    if Check_P == WALL:
                        game.player.move_left()
                        running = True
            if event.key == pygame.K_LEFT:
                game.player.move_left()
                for WALL in check_wall.search('M'):
                    WALL[0] = WALL[0] * scall_screen[0]
                    WALL[1] = WALL[1] * scall_screen[1]
                    Check_P = [game.player.rect.x, game.player.rect.y]
                    if Check_P == WALL:
                        game.player.move_right()
                        running = True
            if event.key == pygame.K_UP:
                game.player.move_up()
                for WALL in check_wall.search('M'):
                    WALL[0] = WALL[0] * scall_screen[0]
                    WALL[1] = WALL[1] * scall_screen[1]
                    Check_P = [game.player.rect.x, game.player.rect.y]
                    if Check_P == WALL:
                        game.player.move_down()
                        running = True
            if event.key == pygame.K_DOWN:
                game.player.move_down()
                for WALL in check_wall.search('M'):
                    WALL[0] = WALL[0] * scall_screen[0]
                    WALL[1] = WALL[1] * scall_screen[1]
                    Check_P = [game.player.rect.x, game.player.rect.y]
                    if Check_P == WALL:
                        game.player.move_up()
                        running = True
        Check_P = [game.player.rect.x, game.player.rect.y]
        if Check_P == GUARD:
            print('YOU WIN')
            import time
            time.sleep(1)
            running = False
            pygame.quit()
