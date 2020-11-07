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
C : The way"""

import pygame
from game import Game

pygame.init()

# generate window's game
pygame.display.set_caption("labyrinth Game")
resolution = [645, 774]
screen = pygame.display.set_mode([resolution[0], resolution[1]])
coeff_screen = [15, 18]
scall_screen = [resolution[0] // coeff_screen[0], resolution[1] // coeff_screen[1]]

# Import Background's picture
background = pygame.image.load('macgyver_ressources/ressource/RDL_FDC.jpeg')

# Import Wall Labyrinth
wall = pygame.image.load('macgyver_ressources/ressource/bricks-small.png')
wall = pygame.transform.scale(wall, (scall_screen[0], scall_screen[1]))

# Import Way Labyrinth
way = pygame.image.load('macgyver_ressources/ressource/tiles-medium.png')
way = pygame.transform.scale(way, (scall_screen[0], scall_screen[1]))

# Import Guardian
Guardian = pygame.image.load('macgyver_ressources/ressource/Gardien.png')
Guardian = pygame.transform.scale(Guardian, (scall_screen[0], scall_screen[1]))

from spawnitems import SpawnItems

# Import Items
Needle_pict = pygame.image.load('macgyver_ressources/ressource/aiguille.PNG')
Needle_pict = pygame.transform.scale(Needle_pict, (scall_screen[0], scall_screen[1]))
plastic_tube_pict = pygame.image.load('macgyver_ressources/ressource/tube_plastique.PNG')
plastic_tube_pict = pygame.transform.scale(plastic_tube_pict, (scall_screen[0], scall_screen[1]))
plastic_tube_pict_int = pygame.image.load('macgyver_ressources/ressource/tube_plastique.PNG')
plastic_tube_pict_int = pygame.transform.scale(plastic_tube_pict, (scall_screen[0], scall_screen[1]))
Ether_pict = pygame.image.load('macgyver_ressources/ressource/ether.PNG')
Ether_pict = pygame.transform.scale(Ether_pict, (scall_screen[0], scall_screen[1]))
Syringe_pict = pygame.image.load('macgyver_ressources/ressource/seringue.PNG')
Syringe_pict = pygame.transform.scale(Syringe_pict, (scall_screen[0], scall_screen[1]))

# Import Lose picture
Lose = pygame.image.load('macgyver_ressources/ressource/loser.PNG')

# Import Victory picture
Win = pygame.image.load('macgyver_ressources/ressource/victoire.JPG')

from find import Find

check_gard = Find()
for GUARD in check_gard.search('S'):
    GUARD[0] = GUARD[0] * scall_screen[0]
    GUARD[1] = GUARD[1] * scall_screen[1]

# Import wall position
check_wall = Find()

# Import way position
check_way = Find()

# Item position
Nee = Find()
Pla = Find()
Eth = Find()

# Load Game
game = Game()

running = True

# repeat for test

count_object = ["", "", ""]

while running:

    # Background position
    screen.blit(background, (-450, -100))

    # Wall picture
    for WALL in check_wall.search('M'):
        WALL[0] = WALL[0] * scall_screen[0]
        WALL[1] = WALL[1] * scall_screen[1]
        screen.blit(wall, ((WALL[0]), (WALL[1])))
    for WALL in check_wall.search('W'):
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

    # Items position
    Check_P = [game.player.rect.x, game.player.rect.y]

    print(count_object)

    for NEE in Nee.search('N'):
        NEE[0] = NEE[0] * scall_screen[0]
        NEE[1] = NEE[1] * scall_screen[1]
        screen.blit(Needle_pict, (NEE[0], NEE[1]))

    screen.blit(Needle_pict, SpawnItems.needle)
    if SpawnItems.needle == Check_P:
        Needle_pict = way
        count_object[0] = ["N"]


    for PLA in Pla.search('P'):
        PLA[0] = PLA[0] * scall_screen[0]
        PLA[1] = PLA[1] * scall_screen[1]
        screen.blit(plastic_tube_pict_int, (PLA[0], PLA[1]))
    screen.blit(plastic_tube_pict, SpawnItems.plastic_tube)
    if SpawnItems.plastic_tube == Check_P:
        plastic_tube_pict = way
        plastic_tube_pict_int = way
        count_object[1] = ["S"]


    for ETH in Eth.search('G'):
        ETH[0] = ETH[0] * scall_screen[0]
        ETH[1] = ETH[1] * scall_screen[1]
        screen.blit(Ether_pict, (ETH[0], ETH[1]))
    screen.blit(Ether_pict, SpawnItems.ether)
    if SpawnItems.ether == Check_P:
        Ether_pict = way
        count_object[2] = ["E"]


    # Player's picture
    screen.blit(game.player.image, game.player.rect)

    # MAJ screen
    pygame.display.flip()

    if count_object == [['N'], ['S'], ['E']]:
        plastic_tube_pict_int = Syringe_pict

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
            if count_object == [["N"], ["S"], ["E"]]:
                print('YOU WIN')
                screen.blit(Win, (0, 0))
                import time
                time.sleep(2)
                running = False
                pygame.quit()
            else:
                print("YOU LOSE")
                screen.blit(Lose, (0, 0))
                import time
                time.sleep(2)
                running = False
                pygame.quit()
