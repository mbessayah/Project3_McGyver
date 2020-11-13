# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

""" OBJ : Create a labyrinth game
    MacGyver must to leave the labyrinth with three objects

Attribute letters in labyrinth.txt file

D : Start position (Mac_Gyver)
S : End position (Guardian)
M : The wall
C : The way"""

import pygame

from models.game import Game

pygame.init()

# generate window's game

from views.screen import Screen

from models.spawnitems import SpawnItems

from controllers.find import Find

from views.picture_song import PictureSong

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

    # Read Song
    PictureSong.Game_song.play(0, 0, 0)
    PictureSong.Game_song.set_volume(0.01)

    # Background position
    Screen.screen.blit(Screen.background, (-450, -100))

    # Wall picture
    for WALL in check_wall.search('M'):
        WALL[0] = WALL[0] * Screen.scall_screen[0]
        WALL[1] = WALL[1] * Screen.scall_screen[1]
        Screen.screen.blit(PictureSong.wall, ((WALL[0]), (WALL[1])))
    for WALL in check_wall.search('W'):
        WALL[0] = WALL[0] * Screen.scall_screen[0]
        WALL[1] = WALL[1] * Screen.scall_screen[1]
        Screen.screen.blit(PictureSong.wall, ((WALL[0]), (WALL[1])))

    # Way picture
    for WAY in check_way.search('C'):
        WAY[0] = WAY[0] * Screen.scall_screen[0]
        WAY[1] = WAY[1] * Screen.scall_screen[1]
        Screen.screen.blit(PictureSong.way, ((WAY[0]), (WAY[1])))
    for WAY in check_way.search('D'):
        WAY[0] = WAY[0] * Screen.scall_screen[0]
        WAY[1] = WAY[1] * Screen.scall_screen[1]
        Screen.screen.blit(PictureSong.way, ((WAY[0]), (WAY[1])))
    for WAY in check_way.search('S'):
        WAY[0] = WAY[0] * Screen.scall_screen[0]
        WAY[1] = WAY[1] * Screen.scall_screen[1]
        Screen.screen.blit(PictureSong.way, ((WAY[0]), (WAY[1])))

    # Guardian position
    Screen.screen.blit(PictureSong.Guardian, ((game.GUARD[0]), (game.GUARD[1])))

    # Items position
    Check_P = [game.player.rect.x, game.player.rect.y]
    from views.picture_song import PictureSong

    for NEE in Nee.search('N'):
        NEE[0] = NEE[0] * Screen.scall_screen[0]
        NEE[1] = NEE[1] * Screen.scall_screen[1]
        Screen.screen.blit(PictureSong.Needle_pict, (NEE[0], NEE[1]))
    Screen.screen.blit(PictureSong.Needle_pict, SpawnItems.needle)
    if SpawnItems.needle == Check_P:
        PictureSong.Needle_pict = PictureSong.way
        count_object[0] = ["N"]

    for PLA in Pla.search('P'):
        PLA[0] = PLA[0] * Screen.scall_screen[0]
        PLA[1] = PLA[1] * Screen.scall_screen[1]
        Screen.screen.blit(PictureSong.plastic_tube_pict_int, (PLA[0], PLA[1]))
    Screen.screen.blit(PictureSong.plastic_tube_pict, SpawnItems.plastic_tube)
    if SpawnItems.plastic_tube == Check_P:
        PictureSong.plastic_tube_pict = PictureSong.way
        PictureSong.plastic_tube_pict_int = PictureSong.way
        count_object[1] = ["S"]

    for ETH in Eth.search('G'):
        ETH[0] = ETH[0] * Screen.scall_screen[0]
        ETH[1] = ETH[1] * Screen.scall_screen[1]
        Screen.screen.blit(PictureSong.Ether_pict, (ETH[0], ETH[1]))
    Screen.screen.blit(PictureSong.Ether_pict, SpawnItems.ether)
    if SpawnItems.ether == Check_P:
        PictureSong.Ether_pict = PictureSong.way
        count_object[2] = ["E"]

    # Player's picture
    Screen.screen.blit(game.player.image, game.player.rect)

    # MAJ screen
    pygame.display.flip()

    if count_object == [['N'], ['S'], ['E']]:
        PictureSong.plastic_tube_pict_int = PictureSong.Syringe_pict

    # player action
    for event in pygame.event.get():
        # if event closed the window
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            # what button was pushed
            if event.key == pygame.K_RIGHT:
                game.player.move_right()
                for WALL in check_wall.search('M'):
                    WALL[0] = WALL[0] * Screen.scall_screen[0]
                    WALL[1] = WALL[1] * Screen.scall_screen[1]
                    Check_P = [game.player.rect.x, game.player.rect.y]
                    if Check_P == WALL:
                        game.player.move_left()
                        running = True
            if event.key == pygame.K_LEFT:
                game.player.move_left()
                for WALL in check_wall.search('M'):
                    WALL[0] = WALL[0] * Screen.scall_screen[0]
                    WALL[1] = WALL[1] * Screen.scall_screen[1]
                    Check_P = [game.player.rect.x, game.player.rect.y]
                    if Check_P == WALL:
                        game.player.move_right()
                        running = True
            if event.key == pygame.K_UP:
                game.player.move_up()
                for WALL in check_wall.search('M'):
                    WALL[0] = WALL[0] * Screen.scall_screen[0]
                    WALL[1] = WALL[1] * Screen.scall_screen[1]
                    Check_P = [game.player.rect.x, game.player.rect.y]
                    if Check_P == WALL:
                        game.player.move_down()
                        running = True
            if event.key == pygame.K_DOWN:
                game.player.move_down()
                for WALL in check_wall.search('M'):
                    WALL[0] = WALL[0] * Screen.scall_screen[0]
                    WALL[1] = WALL[1] * Screen.scall_screen[1]
                    Check_P = [game.player.rect.x, game.player.rect.y]
                    if Check_P == WALL:
                        game.player.move_up()
                        running = True
        Check_P = [game.player.rect.x, game.player.rect.y]
        if Check_P == game.GUARD:
            if count_object == [["N"], ["S"], ["E"]]:
                Screen.screen.blit(PictureSong.Win, (0, 0))
                pygame.display.update()
                PictureSong.Game_song.stop()
                PictureSong.Win_song.play(0, 0, 1000)
                PictureSong.Win_song.set_volume(0.1)
                import time

                time.sleep(7)
                running = False
                pygame.quit()
            else:
                Screen.screen.blit(PictureSong.Lose, (0, 0))
                pygame.display.update()
                PictureSong.Game_song.stop()
                PictureSong.Lose_song.play(0, 0, 5000)
                PictureSong.Lose_song.set_volume(0.1)
                import time

                time.sleep(10)
                running = False
                pygame.quit()
