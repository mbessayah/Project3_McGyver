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
        from main import scall_screen

        self.image = pygame.image.load('macgyver_ressources/ressource/MacGyver.png')
        self.image = pygame.transform.scale(self.image, (scall_screen[0], scall_screen[1]))
        self.rect = self.image.get_rect()
        self.rect.x = (MAC[0] * scall_screen[0])
        self.rect.y = (MAC[1] * scall_screen[1])
        self.velocity = scall_screen[0]

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity

