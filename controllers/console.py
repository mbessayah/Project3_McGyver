# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes,
# files, tool windows, actions, and settings.

""" This module contains Console class.
This class manages the labyrinth interface."""

import time
import pygame

from views.screen import Screen
from views import picture_song
from controllers import find, player
from models import guardian, spawnitems

# Load Game
PLAYER = player.Player()
GUARDIAN = guardian.Guardian()
PICT_SON = picture_song.PictureSong()
ITEM = spawnitems.SpawnItems()


class Console:
    """ Manage labyrinth interface """

    def __init__(self):
        """ Constructor """
        self.check_all = find.Find()
        self.count_object = ["", "", ""]

    def struc_laby(self):
        """ Read Song """
        PICT_SON.Game_song.play(0, 0, 0)
        PICT_SON.Game_song.set_volume(0.01)
        # Wall picture
        self.struc_wall('M')
        self.struc_wall('W')
        # Way picture
        self.struc_way('C')
        self.struc_way('D')
        self.struc_way('S')
        # Guardian position
        Screen.screen.blit(PICT_SON.Guardian, (
            (GUARDIAN.GUARD[0]), (GUARDIAN.GUARD[1])))

    def struc_wall(self, req):
        """ Wall position & picture """
        for wall in self.check_all.search(req):
            wall[0] = wall[0] * Screen.scall_screen[0]
            wall[1] = wall[1] * Screen.scall_screen[1]
            Screen.screen.blit(PICT_SON.wall, ((wall[0]), (wall[1])))

    def struc_way(self, req):
        """ Way position & picture """
        for way in self.check_all.search(req):
            way[0] = way[0] * Screen.scall_screen[0]
            way[1] = way[1] * Screen.scall_screen[1]
            Screen.screen.blit(PICT_SON.way, ((way[0]), (way[1])))

    def items(self):
        """ Items position """
        check_p = [PLAYER.rect.x, PLAYER.rect.y]

        for nee in self.check_all.search('N'):
            nee[0] = nee[0] * Screen.scall_screen[0]
            nee[1] = nee[1] * Screen.scall_screen[1]
            Screen.screen.blit(PICT_SON.Needle_pict, (nee[0], nee[1]))
        Screen.screen.blit(PICT_SON.Needle_pict, ITEM.needle_ch())
        if ITEM.needle_ch() == check_p:
            PICT_SON.Needle_pict = PICT_SON.way
            self.count_object[0] = ["N"]

        for pla in self.check_all.search('P'):
            pla[0] = pla[0] * Screen.scall_screen[0]
            pla[1] = pla[1] * Screen.scall_screen[1]
            Screen.screen.blit(
                PICT_SON.plastic_tube_pict_int, (pla[0], pla[1]))
        Screen.screen.blit(PICT_SON.plastic_tube_pict, ITEM.plastic_ch())
        if ITEM.plastic_ch() == check_p:
            PICT_SON.plastic_tube_pict = PICT_SON.way
            PICT_SON.plastic_tube_pict_int = PICT_SON.way
            self.count_object[1] = ["S"]

        for eth in self.check_all.search('G'):
            eth[0] = eth[0] * Screen.scall_screen[0]
            eth[1] = eth[1] * Screen.scall_screen[1]
            Screen.screen.blit(PICT_SON.Ether_pict, (eth[0], eth[1]))
        Screen.screen.blit(PICT_SON.Ether_pict, ITEM.ether_ch())
        if ITEM.ether_ch() == check_p:
            PICT_SON.Ether_pict = PICT_SON.way
            self.count_object[2] = ["E"]

        # Player's picture
        Screen.screen.blit(PLAYER.image, PLAYER.rect)

        # MAJ screen
        pygame.display.flip()

        if self.count_object == [['N'], ['S'], ['E']]:
            PICT_SON.plastic_tube_pict_int = PICT_SON.Syringe_pict

    def player_action(self):
        """ player action """
        for event in pygame.event.get():
            # if event closed the window
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                # what button was pushed
                if event.key == pygame.K_RIGHT:
                    PLAYER.move_right()
                    self.check_right()
                if event.key == pygame.K_LEFT:
                    PLAYER.move_left()
                    self.check_left()
                if event.key == pygame.K_UP:
                    PLAYER.move_up()
                    self.check_up()
                if event.key == pygame.K_DOWN:
                    PLAYER.move_down()
                    self.check_down()
            check_p = [PLAYER.rect.x, PLAYER.rect.y]
            if check_p == GUARDIAN.GUARD:
                if self.count_object == [["N"], ["S"], ["E"]]:
                    self.win()
                else:
                    self.lose()

    def check_left(self):
        """ check left move and collision """
        for wall in self.check_all.search('M'):
            wall[0] = wall[0] * Screen.scall_screen[0]
            wall[1] = wall[1] * Screen.scall_screen[1]
            check_p = [PLAYER.rect.x, PLAYER.rect.y]
            if check_p == wall:
                PLAYER.move_right()
        return True

    def check_right(self):
        """ check right move and collision """
        for wall in self.check_all.search('M'):
            wall[0] = wall[0] * Screen.scall_screen[0]
            wall[1] = wall[1] * Screen.scall_screen[1]
            check_p = [PLAYER.rect.x, PLAYER.rect.y]
            if check_p == wall:
                PLAYER.move_left()
        return True

    def check_up(self):
        """ check up move and collision """
        for wall in self.check_all.search('M'):
            wall[0] = wall[0] * Screen.scall_screen[0]
            wall[1] = wall[1] * Screen.scall_screen[1]
            check_p = [PLAYER.rect.x, PLAYER.rect.y]
            if check_p == wall:
                PLAYER.move_down()
        return True

    def check_down(self):
        """ check down move and collision """
        for wall in self.check_all.search('M'):
            wall[0] = wall[0] * Screen.scall_screen[0]
            wall[1] = wall[1] * Screen.scall_screen[1]
            check_p = [PLAYER.rect.x, PLAYER.rect.y]
            if check_p == wall:
                PLAYER.move_up()
        return True

    def win(self):
        """ define win condition """
        Screen.screen.blit(PICT_SON.Win, (0, 0))
        pygame.display.update()
        PICT_SON.Game_song.stop()
        PICT_SON.Win_song.play(0, 0, 1000)
        PICT_SON.Win_song.set_volume(0.1)
        time.sleep(4)
        pygame.quit()
        return False

    def lose(self):
        """ define lose condition """
        Screen.screen.blit(PICT_SON.Lose, (0, 0))
        pygame.display.update()
        PICT_SON.Game_song.stop()
        PICT_SON.Lose_song.play(0, 0, 1000)
        PICT_SON.Lose_song.set_volume(0.1)
        time.sleep(10)
        pygame.quit()
        return False

    def start_laby(self):
        """ launch methods """
        while True:
            self.struc_laby()
            self.items()
            self.player_action()
