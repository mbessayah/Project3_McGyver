# !/usr/bin/env python
# -*- coding: utf-8 -*-

""" Control interaction """

from controllers.player import Player

# Game's Class


class Game:

    from controllers.find import Find
    from views.screen import Screen
    check_gard = Find()
    for GUARD in check_gard.search('S'):
        GUARD[0] = (GUARD[0] * Screen.scall_screen[0])
        GUARD[1] = (GUARD[1] * Screen.scall_screen[1])

    def __init__(self):
        # generate player
        self.player = Player()
