# !/usr/bin/env python
# -*- coding: utf-8 -*-

""" Attribute picture for object """

import pygame
from views.screen import Screen


class PictureSong:

    # Song Game
    Game_song = pygame.mixer.Sound("macgyver_ressources/ressource/8bitmcg.ogg")

    # Needle Picture
    Needle_pict = pygame.image.load(
        'macgyver_ressources/ressource/aiguille.PNG')
    Needle_pict = pygame.transform.scale(Needle_pict, (
        Screen.scall_screen[0], Screen.scall_screen[1]))

    # Plastic Tube Picture
    plastic_tube_pict = pygame.image.load(
        'macgyver_ressources/ressource/tube_plastique.PNG')
    plastic_tube_pict = pygame.transform.scale(plastic_tube_pict, (
        Screen.scall_screen[0], Screen.scall_screen[1]))
    plastic_tube_pict_int = pygame.image.load(
        'macgyver_ressources/ressource/tube_plastique.PNG')
    plastic_tube_pict_int = pygame.transform.scale(
        plastic_tube_pict, (Screen.scall_screen[0], Screen.scall_screen[1]))

    # Ether Picture
    Ether_pict = pygame.image.load('macgyver_ressources/ressource/ether.PNG')
    Ether_pict = pygame.transform.scale(
        Ether_pict, (Screen.scall_screen[0], Screen.scall_screen[1]))

    # Syringe Picture
    Syringe_pict = pygame.image.load(
        'macgyver_ressources/ressource/seringue.PNG')
    Syringe_pict = pygame.transform.scale(
        Syringe_pict, (Screen.scall_screen[0], Screen.scall_screen[1]))

    # Import Wall Labyrinth
    wall = pygame.image.load('macgyver_ressources/ressource/bricks-small.png')
    wall = pygame.transform.scale(
        wall, (Screen.scall_screen[0], Screen.scall_screen[1]))

    # Import Way Labyrinth
    way = pygame.image.load('macgyver_ressources/ressource/tiles-medium.png')
    way = pygame.transform.scale(
        way, (Screen.scall_screen[0], Screen.scall_screen[1]))

    # Import Guardian
    Guardian = pygame.image.load(
        'macgyver_ressources/ressource/Gardien.png')
    Guardian = pygame.transform.scale(
        Guardian, (Screen.scall_screen[0], Screen.scall_screen[1]))

    # Import Lose picture
    Lose = pygame.image.load('macgyver_ressources/ressource/lose.JPG')
    Lose = pygame.transform.scale(
        Lose, (Screen.resolution[0], Screen.resolution[1]))
    Lose_song = pygame.mixer.Sound("macgyver_ressources/ressource/Lose.ogg")

    # Import Victory picture
    Win = pygame.image.load('macgyver_ressources/ressource/Victoire.PNG')
    Win = pygame.transform.scale(
        Win, (Screen.resolution[0], Screen.resolution[1]))
    Win_song = pygame.mixer.Sound("macgyver_ressources/ressource/Win.ogg")
