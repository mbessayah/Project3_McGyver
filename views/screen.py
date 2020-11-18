# !/usr/bin/env python
# -*- coding: utf-8 -*-

""" Parameters of screen """

import pygame


class Screen:
    """ use the resolution to assign a divisor coefficient """

    # generate window's game

    pygame.display.set_caption("labyrinth Game")
    resolution = [645, 774]
    screen = pygame.display.set_mode([resolution[0], resolution[1]])
    coeff_screen = [15, 18]
    scall_screen = [
        resolution[0] // coeff_screen[0], resolution[1] // coeff_screen[1]]
