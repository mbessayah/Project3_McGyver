# !/usr/bin/env python
# -*- coding: utf-8 -*-
""" Set the player settings """
import pygame

from controllers.find import Find
from views.screen import Screen

check_mac = Find()
for l_MAC in check_mac.search('D'):
    MAC = l_MAC


class Player(pygame.sprite.Sprite):
    """ Attribute parameters """

    def __init__(self):
        """ image, size & velocity """
        self.image = pygame.image.load('macgyver_ressources/'
                                       'ressource/MacGyver.png')
        self.image = pygame.transform.scale(
            self.image, (Screen.scall_screen[0], Screen.scall_screen[1]))
        self.rect = self.image.get_rect()
        self.rect.x = (MAC[0] * Screen.scall_screen[0])
        self.rect.y = (MAC[1] * Screen.scall_screen[1])
        self.velocity = Screen.scall_screen[0]

    def move_right(self):
        """ def velocity on right """
        self.rect.x += self.velocity

    def move_left(self):
        """ def velocity on left """
        self.rect.x -= self.velocity

    def move_up(self):
        """ def velocity on up """
        self.rect.y -= self.velocity

    def move_down(self):
        """ def velocity on down """
        self.rect.y += self.velocity
