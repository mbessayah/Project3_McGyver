# !/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

from find import Find

check_mac = Find()
for l_MAC in check_mac.search('D'):
    MAC = l_MAC

# Player's Class
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.image = pygame.image.load('macgyver_ressources/ressource/MacGyver.png')
        self.rect = self.image.get_rect()
        self.rect.x = (MAC[0] * 43)
        self.rect.y = (MAC[1] * 43)
        self.velocity = 43

    def move_right(self):
        self.rect.x += self.velocity
    def move_left(self):
        self.rect.x += -self.velocity
    def move_up(self):
        self.rect.y += -self.velocity
    def move_down(self):
        self.rect.y += self.velocity
