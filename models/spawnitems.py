# !/usr/bin/env python
# -*- coding: utf-8 -*-

""" Give aleatory position for items """

import random

from controllers.find import Find
from views.screen import Screen

check_way = Find()


class SpawnItems:
    """ give three randoms positions for objects """
    spawn_items = check_way.search('C')

    for aleatory in range(1):
        Check_Items = (random.sample(spawn_items, 3))

    def needle_ch(self):
        """ position of needle object """
        needle = [SpawnItems.Check_Items[0][0] * Screen.scall_screen[0],
                  SpawnItems.Check_Items[0][1] * Screen.scall_screen[1]]
        return needle

    def plastic_ch(self):
        """ position of plastic object """
        plastic_tube = [SpawnItems.Check_Items[1][0] * Screen.scall_screen[0],
                        SpawnItems.Check_Items[1][1] * Screen.scall_screen[1]]
        return plastic_tube

    def ether_ch(self):
        """ position of ether object """
        ether = [SpawnItems.Check_Items[2][0] * Screen.scall_screen[0],
                 SpawnItems.Check_Items[2][1] * Screen.scall_screen[1]]
        return ether
