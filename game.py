# !/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

from player import Player

# Game's Class
class Game:

    def __init__(self):
        # generate player
        self.player = Player()
